from defoldsdk import sdk
from google.protobuf.descriptor import FieldDescriptor
import json, inspect, os, sys


class SdkGenDoc:
    PROTOBUF_TYPE_TO_PYTHON_TYPE = {
        FieldDescriptor.TYPE_DOUBLE: 'float',
        FieldDescriptor.TYPE_FLOAT: 'float',
        FieldDescriptor.TYPE_INT64: 'int',
        FieldDescriptor.TYPE_UINT64: 'int',
        FieldDescriptor.TYPE_INT32: 'int',
        FieldDescriptor.TYPE_FIXED64: 'int',
        FieldDescriptor.TYPE_FIXED32: 'int',
        FieldDescriptor.TYPE_BOOL: 'bool',
        FieldDescriptor.TYPE_STRING: 'str',
        FieldDescriptor.TYPE_BYTES: 'bytes',
        FieldDescriptor.TYPE_UINT32: 'int',
        FieldDescriptor.TYPE_ENUM: 'int',
        FieldDescriptor.TYPE_SFIXED32: 'int',
        FieldDescriptor.TYPE_SFIXED64: 'int',
        FieldDescriptor.TYPE_SINT32: 'int',
        FieldDescriptor.TYPE_SINT64: 'int',
    }

    @staticmethod
    def get_type_enums(typ):
        enums = {}
        for enum_name, enum_type in typ.DESCRIPTOR.enum_types_by_name.items():
            enums[enum_name] = [f"{key} = {value.number}" for key, value in enum_type.values_by_name.items()]
        return enums

    @staticmethod
    def parse_field(typ, field, name):
        if field.type == field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED:
            field_type = field.message_type._concrete_class.__name__
        elif field.type == field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED:
            field_type = f"List[{field.message_type._concrete_class.__name__}]"
        elif field.type != field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED:
            field_type = f"List[{SdkGenDoc.PROTOBUF_TYPE_TO_PYTHON_TYPE.get(field.type)}]"
        else:
            field_type = SdkGenDoc.PROTOBUF_TYPE_TO_PYTHON_TYPE.get(field.type)
        return {"name": name, "type": field_type}

    @staticmethod
    def parse_fields(typ):
        fields = {}
        for name, field in typ.DESCRIPTOR.fields_by_name.items():
            fields[name] = SdkGenDoc.parse_field(typ=typ, field=field, name=name)
        return fields

    @staticmethod
    def parse_type(typ):
        return {"enums": SdkGenDoc.get_type_enums(typ), "fields": SdkGenDoc.parse_fields(typ)}

    def gen_doc(self, mdfile = "docs/README.md"):
        markdown_lines = ["# SDK Protobuf Documentation\n"]
        for typ_name, typ in sdk._asdict().items():
            info = SdkGenDoc.parse_type(typ)
            markdown_lines.append(f"## Message: `{typ_name}`\n")

            if info["fields"]:
                markdown_lines.append("### Fields:")
                for fname, fdata in info["fields"].items():
                    markdown_lines.append(f"- **{fname}**: `{fdata['type']}`")
            else:
                markdown_lines.append("_No fields_\n")

            if info["enums"]:
                markdown_lines.append("\n### Enums:")
                for enum_name, values in info["enums"].items():
                    markdown_lines.append(f"- **{enum_name}**:")
                    for v in values:
                        markdown_lines.append(f"  - `{v}`")
            markdown_lines.append("\n---\n")

        with open(mdfile, "w") as f:
            f.write("\n".join(markdown_lines))


if __name__ == "__main__":
    SdkGenDoc().gen_doc(mdfile = "docs/README.md")

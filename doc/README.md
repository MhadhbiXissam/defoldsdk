# SDK Protobuf Documentation

## Message: `AcquireCameraFocus`

_No fields_


---

## Message: `AcquireInputFocus`

_No fields_


---

## Message: `Animation`

### Fields:
- **id**: `str`
- **start_tile**: `int`
- **end_tile**: `int`
- **playback**: `int`
- **fps**: `int`
- **flip_horizontal**: `int`
- **flip_vertical**: `int`
- **cues**: `List[Cue]`

---

## Message: `AnimationDone`

### Fields:
- **current_tile**: `int`
- **id**: `int`

---

## Message: `ApplyForce`

### Fields:
- **force**: `Vector3`
- **position**: `Point3`

---

## Message: `Atlas`

### Fields:
- **images**: `List[AtlasImage]`
- **animations**: `List[AtlasAnimation]`
- **margin**: `int`
- **extrude_borders**: `int`
- **inner_padding**: `int`
- **max_page_width**: `int`
- **max_page_height**: `int`
- **rename_patterns**: `str`

---

## Message: `AtlasAnimation`

### Fields:
- **id**: `str`
- **images**: `List[AtlasImage]`
- **playback**: `int`
- **fps**: `int`
- **flip_horizontal**: `int`
- **flip_vertical**: `int`

---

## Message: `AtlasImage`

### Fields:
- **image**: `str`
- **sprite_trim_mode**: `int`
- **pivot_x**: `float`
- **pivot_y**: `float`

---

## Message: `BufferDesc`

### Fields:
- **streams**: `List[StreamDesc]`

---

## Message: `CameraDesc`

### Fields:
- **aspect_ratio**: `float`
- **fov**: `float`
- **near_z**: `float`
- **far_z**: `float`
- **auto_aspect_ratio**: `int`
- **orthographic_projection**: `int`
- **orthographic_zoom**: `float`
- **orthographic_mode**: `int`

---

## Message: `ClearColor`

### Fields:
- **color**: `Vector4`

---

## Message: `CollectionDesc`

### Fields:
- **name**: `str`
- **instances**: `List[InstanceDesc]`
- **collection_instances**: `List[CollectionInstanceDesc]`
- **scale_along_z**: `int`
- **embedded_instances**: `List[EmbeddedInstanceDesc]`
- **property_resources**: `List[str]`
- **component_types**: `List[ComponenTypeDesc]`

---

## Message: `CollectionFactoryDesc`

### Fields:
- **prototype**: `str`
- **load_dynamically**: `bool`
- **dynamic_prototype**: `bool`

---

## Message: `CollectionInstanceDesc`

### Fields:
- **id**: `str`
- **collection**: `str`
- **position**: `Point3`
- **rotation**: `Quat`
- **scale**: `float`
- **scale3**: `Vector3One`
- **instance_properties**: `List[InstancePropertyDesc]`

---

## Message: `CollectionProxyDesc`

### Fields:
- **collection**: `str`
- **exclude**: `bool`

---

## Message: `Collision`

### Fields:
- **position**: `Point3`
- **id**: `int`
- **group**: `int`

---

## Message: `CollisionEvent`

### Fields:
- **a**: `Collision`
- **b**: `Collision`

---

## Message: `CollisionObjectDesc`

### Fields:
- **collision_shape**: `str`
- **type**: `int`
- **mass**: `float`
- **friction**: `float`
- **restitution**: `float`
- **group**: `str`
- **mask**: `List[str]`
- **embedded_collision_shape**: `CollisionShape`
- **linear_damping**: `float`
- **angular_damping**: `float`
- **locked_rotation**: `bool`
- **bullet**: `bool`
- **event_collision**: `bool`
- **event_contact**: `bool`
- **event_trigger**: `bool`

---

## Message: `CollisionResponse`

### Fields:
- **other_id**: `int`
- **group**: `int`
- **other_position**: `Point3`
- **other_group**: `int`
- **own_group**: `int`

---

## Message: `CollisionShape`

### Fields:
- **shapes**: `List[Shape]`
- **data**: `List[float]`

### Enums:
- **Type**:
  - `TYPE_SPHERE = 0`
  - `TYPE_BOX = 1`
  - `TYPE_CAPSULE = 2`
  - `TYPE_HULL = 3`

---

## Message: `ComponenTypeDesc`

### Fields:
- **name_hash**: `int`
- **max_count**: `int`

---

## Message: `ComponentDesc`

### Fields:
- **id**: `str`
- **component**: `str`
- **position**: `Point3`
- **rotation**: `Quat`
- **properties**: `List[PropertyDesc]`
- **property_decls**: `PropertyDeclarations`
- **scale**: `Vector3One`

---

## Message: `ComponentPropertyDesc`

### Fields:
- **id**: `str`
- **properties**: `List[PropertyDesc]`
- **property_decls**: `PropertyDeclarations`

---

## Message: `ContactPoint`

### Fields:
- **position**: `Point3`
- **instance_position**: `Point3`
- **normal**: `Vector3`
- **relative_velocity**: `Vector3`
- **mass**: `float`
- **id**: `int`
- **group**: `int`

---

## Message: `ContactPointEvent`

### Fields:
- **a**: `ContactPoint`
- **b**: `ContactPoint`
- **distance**: `float`
- **applied_impulse**: `float`

---

## Message: `ContactPointResponse`

### Fields:
- **position**: `Point3`
- **normal**: `Vector3`
- **relative_velocity**: `Vector3`
- **distance**: `float`
- **applied_impulse**: `float`
- **life_time**: `float`
- **mass**: `float`
- **other_mass**: `float`
- **other_id**: `int`
- **other_position**: `Point3`
- **group**: `int`
- **other_group**: `int`
- **own_group**: `int`

---

## Message: `ConvexHull`

### Fields:
- **index**: `int`
- **count**: `int`
- **collision_group**: `str`

---

## Message: `ConvexShape`

### Fields:
- **shape_type**: `int`
- **data**: `List[float]`

### Enums:
- **Type**:
  - `TYPE_SPHERE = 0`
  - `TYPE_BOX = 1`
  - `TYPE_CAPSULE = 2`
  - `TYPE_HULL = 3`

---

## Message: `Create`

### Fields:
- **position**: `Point3`
- **rotation**: `Quat`
- **id**: `int`
- **scale**: `float`
- **scale3**: `Vector3`

---

## Message: `Cubemap`

### Fields:
- **right**: `str`
- **left**: `str`
- **top**: `str`
- **bottom**: `str`
- **front**: `str`
- **back**: `str`

---

## Message: `Cue`

### Fields:
- **id**: `str`
- **frame**: `int`
- **value**: `float`

---

## Message: `Disable`

_No fields_


---

## Message: `DisplayProfile`

### Fields:
- **name**: `str`
- **qualifiers**: `List[DisplayProfileQualifier]`

---

## Message: `DisplayProfileQualifier`

### Fields:
- **width**: `int`
- **height**: `int`
- **device_models**: `List[str]`

---

## Message: `DisplayProfiles`

### Fields:
- **profiles**: `List[DisplayProfile]`
- **auto_layout_selection**: `bool`

---

## Message: `DrawDebugText`

### Fields:
- **position**: `Point3`
- **text**: `str`
- **color**: `Vector4`

---

## Message: `DrawLine`

### Fields:
- **start_point**: `Point3`
- **end_point**: `Point3`
- **color**: `Vector4`

---

## Message: `DrawText`

### Fields:
- **position**: `Point3`
- **text**: `str`

---

## Message: `EmbeddedComponentDesc`

### Fields:
- **id**: `str`
- **type**: `str`
- **data**: `str`
- **position**: `Point3`
- **rotation**: `Quat`
- **scale**: `Vector3One`

---

## Message: `EmbeddedInstanceDesc`

### Fields:
- **id**: `str`
- **children**: `List[str]`
- **data**: `str`
- **position**: `Point3`
- **rotation**: `Quat`
- **component_properties**: `List[ComponentPropertyDesc]`
- **scale**: `float`
- **scale3**: `Vector3One`

---

## Message: `Enable`

_No fields_


---

## Message: `EnableGridShapeLayer`

### Fields:
- **shape**: `int`
- **enable**: `int`

---

## Message: `Exit`

### Fields:
- **code**: `int`

---

## Message: `FactoryDesc`

### Fields:
- **prototype**: `str`
- **load_dynamically**: `bool`
- **dynamic_prototype**: `bool`

---

## Message: `FontDesc`

### Fields:
- **font**: `str`
- **material**: `str`
- **size**: `int`
- **antialias**: `int`
- **alpha**: `float`
- **outline_alpha**: `float`
- **outline_width**: `float`
- **shadow_alpha**: `float`
- **shadow_blur**: `int`
- **shadow_x**: `float`
- **shadow_y**: `float`
- **extra_characters**: `str`
- **output_format**: `int`
- **all_chars**: `bool`
- **cache_width**: `int`
- **cache_height**: `int`
- **render_mode**: `int`
- **characters**: `str`

---

## Message: `FontMap`

### Fields:
- **material**: `str`
- **glyph_bank**: `str`
- **font**: `str`
- **size**: `int`
- **antialias**: `int`
- **shadow_x**: `float`
- **shadow_y**: `float`
- **shadow_blur**: `int`
- **shadow_alpha**: `float`
- **alpha**: `float`
- **outline_alpha**: `float`
- **outline_width**: `float`
- **layer_mask**: `int`
- **output_format**: `int`
- **render_mode**: `int`
- **all_chars**: `bool`
- **characters**: `str`
- **cache_width**: `int`
- **cache_height**: `int`
- **sdf_spread**: `float`
- **sdf_outline**: `float`
- **sdf_shadow**: `float`
- **padding**: `int`

---

## Message: `GlyphBank`

### Fields:
- **glyphs**: `List[Glyph]`
- **glyph_padding**: `int`
- **glyph_channels**: `int`
- **glyph_data**: `bytes`
- **max_ascent**: `float`
- **max_descent**: `float`
- **max_advance**: `float`
- **max_width**: `float`
- **max_height**: `float`
- **image_format**: `int`
- **sdf_spread**: `float`
- **sdf_outline**: `float`
- **sdf_shadow**: `float`
- **cache_width**: `int`
- **cache_height**: `int`
- **cache_cell_width**: `int`
- **cache_cell_height**: `int`
- **cache_cell_max_ascent**: `int`
- **padding**: `int`
- **is_monospaced**: `bool`

---

## Message: `HashDigest`

### Fields:
- **data**: `bytes`

---

## Message: `HideApp`

_No fields_


---

## Message: `InstanceDesc`

### Fields:
- **id**: `str`
- **prototype**: `str`
- **children**: `List[str]`
- **position**: `Point3`
- **rotation**: `Quat`
- **component_properties**: `List[ComponentPropertyDesc]`
- **scale**: `float`
- **scale3**: `Vector3One`

---

## Message: `InstancePropertyDesc`

### Fields:
- **id**: `str`
- **properties**: `List[ComponentPropertyDesc]`

---

## Message: `LabelDesc`

### Fields:
- **size**: `Vector4`
- **scale**: `Vector4One`
- **color**: `Vector4One`
- **outline**: `Vector4WOne`
- **shadow**: `Vector4WOne`
- **leading**: `float`
- **tracking**: `float`
- **pivot**: `int`
- **blend_mode**: `int`
- **line_break**: `bool`
- **text**: `str`
- **font**: `str`
- **material**: `str`

### Enums:
- **BlendMode**:
  - `BLEND_MODE_ALPHA = 0`
  - `BLEND_MODE_ADD = 1`
  - `BLEND_MODE_MULT = 3`
  - `BLEND_MODE_SCREEN = 4`
- **Pivot**:
  - `PIVOT_CENTER = 0`
  - `PIVOT_N = 1`
  - `PIVOT_NE = 2`
  - `PIVOT_E = 3`
  - `PIVOT_SE = 4`
  - `PIVOT_S = 5`
  - `PIVOT_SW = 6`
  - `PIVOT_W = 7`
  - `PIVOT_NW = 8`

---

## Message: `LayoutChanged`

### Fields:
- **id**: `int`
- **previous_id**: `int`

---

## Message: `LightDesc`

### Fields:
- **id**: `str`
- **type**: `int`
- **intensity**: `float`
- **color**: `Vector3`
- **range**: `float`
- **decay**: `float`
- **cone_angle**: `float`
- **penumbra_angle**: `float`
- **drop_off**: `float`

---

## Message: `LuaModule`

### Fields:
- **source**: `LuaSource`
- **modules**: `List[str]`
- **resources**: `List[str]`
- **properties**: `PropertyDeclarations`
- **property_resources**: `List[str]`

---

## Message: `LuaRef`

### Fields:
- **ref**: `int`
- **context_table_ref**: `int`

---

## Message: `LuaSource`

### Fields:
- **script**: `bytes`
- **filename**: `str`
- **bytecode**: `bytes`
- **delta**: `bytes`
- **bytecode_32**: `bytes`
- **bytecode_64**: `bytes`

---

## Message: `ManifestData`

### Fields:
- **header**: `ManifestHeader`
- **engine_versions**: `List[HashDigest]`
- **resources**: `List[ResourceEntry]`

---

## Message: `ManifestFile`

### Fields:
- **data**: `bytes`
- **signature**: `bytes`
- **archive_identifier**: `bytes`
- **version**: `int`

---

## Message: `ManifestHeader`

### Fields:
- **resource_hash_algorithm**: `int`
- **signature_hash_algorithm**: `int`
- **signature_sign_algorithm**: `int`
- **project_identifier**: `HashDigest`

---

## Message: `Material`

### Fields:
- **name**: `str`
- **material**: `str`
- **textures**: `List[Texture]`
- **attributes**: `List[VertexAttribute]`

---

## Message: `MaterialDesc`

### Fields:
- **name**: `str`
- **tags**: `List[str]`
- **vertex_program**: `str`
- **fragment_program**: `str`
- **vertex_space**: `int`
- **vertex_constants**: `List[Constant]`
- **fragment_constants**: `List[Constant]`
- **textures**: `List[str]`
- **samplers**: `List[Sampler]`
- **max_page_count**: `int`
- **attributes**: `List[VertexAttribute]`
- **program**: `str`
- **pbr_parameters**: `PbrParameters`

### Enums:
- **ConstantType**:
  - `CONSTANT_TYPE_USER = 0`
  - `CONSTANT_TYPE_VIEWPROJ = 1`
  - `CONSTANT_TYPE_WORLD = 2`
  - `CONSTANT_TYPE_TEXTURE = 3`
  - `CONSTANT_TYPE_VIEW = 4`
  - `CONSTANT_TYPE_PROJECTION = 5`
  - `CONSTANT_TYPE_NORMAL = 6`
  - `CONSTANT_TYPE_WORLDVIEW = 7`
  - `CONSTANT_TYPE_WORLDVIEWPROJ = 8`
  - `CONSTANT_TYPE_USER_MATRIX4 = 9`
- **VertexSpace**:
  - `VERTEX_SPACE_WORLD = 0`
  - `VERTEX_SPACE_LOCAL = 1`
- **WrapMode**:
  - `WRAP_MODE_REPEAT = 0`
  - `WRAP_MODE_MIRRORED_REPEAT = 1`
  - `WRAP_MODE_CLAMP_TO_EDGE = 2`
- **FilterModeMin**:
  - `FILTER_MODE_MIN_NEAREST = 0`
  - `FILTER_MODE_MIN_LINEAR = 1`
  - `FILTER_MODE_MIN_NEAREST_MIPMAP_NEAREST = 2`
  - `FILTER_MODE_MIN_NEAREST_MIPMAP_LINEAR = 3`
  - `FILTER_MODE_MIN_LINEAR_MIPMAP_NEAREST = 4`
  - `FILTER_MODE_MIN_LINEAR_MIPMAP_LINEAR = 5`
  - `FILTER_MODE_MIN_DEFAULT = 6`
- **FilterModeMag**:
  - `FILTER_MODE_MAG_NEAREST = 0`
  - `FILTER_MODE_MAG_LINEAR = 1`
  - `FILTER_MODE_MAG_DEFAULT = 2`

---

## Message: `Matrix4`

### Fields:
- **m00**: `float`
- **m01**: `float`
- **m02**: `float`
- **m03**: `float`
- **m10**: `float`
- **m11**: `float`
- **m12**: `float`
- **m13**: `float`
- **m20**: `float`
- **m21**: `float`
- **m22**: `float`
- **m23**: `float`
- **m30**: `float`
- **m31**: `float`
- **m32**: `float`
- **m33**: `float`

---

## Message: `MeshDesc`

### Fields:
- **material**: `str`
- **vertices**: `str`
- **textures**: `List[str]`
- **primitive_type**: `int`
- **position_stream**: `str`
- **normal_stream**: `str`

### Enums:
- **PrimitiveType**:
  - `PRIMITIVE_LINES = 1`
  - `PRIMITIVE_TRIANGLES = 4`
  - `PRIMITIVE_TRIANGLE_STRIP = 5`

---

## Message: `Model`

### Fields:
- **rig_scene**: `str`
- **default_animation**: `str`
- **materials**: `List[Material]`
- **create_go_bones**: `bool`

---

## Message: `ModelAnimationDone`

### Fields:
- **animation_id**: `int`
- **playback**: `int`

---

## Message: `ModelCancelAnimation`

_No fields_


---

## Message: `ModelDesc`

### Fields:
- **mesh**: `str`
- **material**: `str`
- **textures**: `List[str]`
- **skeleton**: `str`
- **animations**: `str`
- **default_animation**: `str`
- **name**: `str`
- **materials**: `List[Material]`
- **create_go_bones**: `bool`

---

## Message: `ModelPlayAnimation`

### Fields:
- **animation_id**: `int`
- **playback**: `int`
- **blend_duration**: `float`
- **offset**: `float`
- **playback_rate**: `float`

---

## Message: `NodeDesc`

### Fields:
- **position**: `Vector4`
- **rotation**: `Vector4`
- **scale**: `Vector4One`
- **size**: `Vector4`
- **color**: `Vector4One`
- **type**: `int`
- **blend_mode**: `int`
- **text**: `str`
- **texture**: `str`
- **font**: `str`
- **id**: `str`
- **xanchor**: `int`
- **yanchor**: `int`
- **pivot**: `int`
- **outline**: `Vector4WOne`
- **shadow**: `Vector4WOne`
- **adjust_mode**: `int`
- **line_break**: `bool`
- **parent**: `str`
- **layer**: `str`
- **inherit_alpha**: `bool`
- **slice9**: `Vector4`
- **outerBounds**: `int`
- **innerRadius**: `float`
- **perimeterVertices**: `int`
- **pieFillAngle**: `float`
- **clipping_mode**: `int`
- **clipping_visible**: `bool`
- **clipping_inverted**: `bool`
- **alpha**: `float`
- **outline_alpha**: `float`
- **shadow_alpha**: `float`
- **overridden_fields**: `List[int]`
- **template**: `str`
- **template_node_child**: `bool`
- **text_leading**: `float`
- **text_tracking**: `float`
- **size_mode**: `int`
- **spine_scene**: `str`
- **spine_default_animation**: `str`
- **spine_skin**: `str`
- **spine_node_child**: `bool`
- **particlefx**: `str`
- **custom_type**: `int`
- **enabled**: `bool`
- **visible**: `bool`
- **material**: `str`

### Enums:
- **Type**:
  - `TYPE_BOX = 0`
  - `TYPE_TEXT = 1`
  - `TYPE_PIE = 2`
  - `TYPE_TEMPLATE = 3`
  - `TYPE_SPINE = 4`
  - `TYPE_PARTICLEFX = 5`
  - `TYPE_CUSTOM = 6`
- **BlendMode**:
  - `BLEND_MODE_ALPHA = 0`
  - `BLEND_MODE_ADD = 1`
  - `BLEND_MODE_ADD_ALPHA = 2`
  - `BLEND_MODE_MULT = 3`
  - `BLEND_MODE_SCREEN = 4`
- **ClippingMode**:
  - `CLIPPING_MODE_NONE = 0`
  - `CLIPPING_MODE_STENCIL = 2`
- **XAnchor**:
  - `XANCHOR_NONE = 0`
  - `XANCHOR_LEFT = 1`
  - `XANCHOR_RIGHT = 2`
- **YAnchor**:
  - `YANCHOR_NONE = 0`
  - `YANCHOR_TOP = 1`
  - `YANCHOR_BOTTOM = 2`
- **Pivot**:
  - `PIVOT_CENTER = 0`
  - `PIVOT_N = 1`
  - `PIVOT_NE = 2`
  - `PIVOT_E = 3`
  - `PIVOT_SE = 4`
  - `PIVOT_S = 5`
  - `PIVOT_SW = 6`
  - `PIVOT_W = 7`
  - `PIVOT_NW = 8`
- **AdjustMode**:
  - `ADJUST_MODE_FIT = 0`
  - `ADJUST_MODE_ZOOM = 1`
  - `ADJUST_MODE_STRETCH = 2`
- **SizeMode**:
  - `SIZE_MODE_MANUAL = 0`
  - `SIZE_MODE_AUTO = 1`
- **PieBounds**:
  - `PIEBOUNDS_RECTANGLE = 0`
  - `PIEBOUNDS_ELLIPSE = 1`

---

## Message: `PathSettings`

### Fields:
- **path**: `str`
- **profile**: `str`

---

## Message: `PauseSound`

### Fields:
- **pause**: `bool`

---

## Message: `PlatformProfile`

### Fields:
- **os**: `int`
- **formats**: `List[TextureFormatAlternative]`
- **mipmaps**: `bool`
- **max_texture_size**: `int`
- **premultiply_alpha**: `bool`

### Enums:
- **OS**:
  - `OS_ID_GENERIC = 0`
  - `OS_ID_WINDOWS = 1`
  - `OS_ID_OSX = 2`
  - `OS_ID_LINUX = 3`
  - `OS_ID_IOS = 4`
  - `OS_ID_ANDROID = 5`
  - `OS_ID_WEB = 6`
  - `OS_ID_SWITCH = 7`
  - `OS_ID_PS4 = 8`
  - `OS_ID_PS5 = 9`
  - `OS_ID_XBOX = 10`

---

## Message: `PlayAnimation`

### Fields:
- **id**: `int`
- **offset**: `float`
- **playback_rate**: `float`

---

## Message: `PlayParticleFX`

_No fields_


---

## Message: `PlaySound`

### Fields:
- **delay**: `float`
- **gain**: `float`
- **pan**: `float`
- **speed**: `float`
- **play_id**: `int`
- **start_time**: `float`
- **start_frame**: `int`

---

## Message: `Point3`

### Fields:
- **x**: `float`
- **y**: `float`
- **z**: `float`
- **d**: `float`

---

## Message: `PropertyDeclarationEntry`

### Fields:
- **key**: `str`
- **id**: `int`
- **index**: `int`
- **element_ids**: `List[int]`

---

## Message: `PropertyDeclarations`

### Fields:
- **number_entries**: `List[PropertyDeclarationEntry]`
- **hash_entries**: `List[PropertyDeclarationEntry]`
- **url_entries**: `List[PropertyDeclarationEntry]`
- **vector3_entries**: `List[PropertyDeclarationEntry]`
- **vector4_entries**: `List[PropertyDeclarationEntry]`
- **quat_entries**: `List[PropertyDeclarationEntry]`
- **bool_entries**: `List[PropertyDeclarationEntry]`
- **float_values**: `List[float]`
- **hash_values**: `List[int]`
- **string_values**: `List[str]`

---

## Message: `PropertyDesc`

### Fields:
- **id**: `str`
- **value**: `str`
- **type**: `int`

---

## Message: `PrototypeDesc`

### Fields:
- **components**: `List[ComponentDesc]`
- **embedded_components**: `List[EmbeddedComponentDesc]`
- **property_resources**: `List[str]`

---

## Message: `Quat`

### Fields:
- **x**: `float`
- **y**: `float`
- **z**: `float`
- **w**: `float`

---

## Message: `RayCastMissed`

### Fields:
- **request_id**: `int`

---

## Message: `RayCastResponse`

### Fields:
- **fraction**: `float`
- **position**: `Point3`
- **normal**: `Vector3`
- **id**: `int`
- **group**: `int`
- **request_id**: `int`

---

## Message: `Reboot`

### Fields:
- **arg1**: `str`
- **arg2**: `str`
- **arg3**: `str`
- **arg4**: `str`
- **arg5**: `str`
- **arg6**: `str`

---

## Message: `ReleaseCameraFocus`

_No fields_


---

## Message: `ReleaseInputFocus`

_No fields_


---

## Message: `Reload`

### Fields:
- **resources**: `List[str]`

---

## Message: `RenderPrototypeDesc`

### Fields:
- **script**: `str`
- **materials**: `List[MaterialDesc]`
- **render_resources**: `List[RenderResourceDesc]`

---

## Message: `RequestRayCast`

### Fields:
- **from**: `Point3`
- **to**: `Point3`
- **mask**: `int`
- **request_id**: `int`

---

## Message: `RequestVelocity`

_No fields_


---

## Message: `ResetConstant`

### Fields:
- **name_hash**: `int`

---

## Message: `ResetConstantParticleFX`

### Fields:
- **emitter_id**: `int`
- **name_hash**: `int`

---

## Message: `ResetConstantTileMap`

### Fields:
- **name_hash**: `int`

---

## Message: `Resize`

### Fields:
- **width**: `int`
- **height**: `int`

---

## Message: `ResourceEntry`

### Fields:
- **hash**: `HashDigest`
- **url**: `str`
- **url_hash**: `int`
- **size**: `int`
- **compressed_size**: `int`
- **flags**: `int`
- **dependants**: `List[int]`

---

## Message: `ResumeRendering`

_No fields_


---

## Message: `RunScript`

### Fields:
- **module**: `LuaModule`

---

## Message: `SceneDesc`

### Fields:
- **script**: `str`
- **fonts**: `List[FontDesc]`
- **textures**: `List[TextureDesc]`
- **background_color**: `Vector4`
- **nodes**: `List[NodeDesc]`
- **layers**: `List[LayerDesc]`
- **material**: `str`
- **layouts**: `List[LayoutDesc]`
- **adjust_reference**: `int`
- **max_nodes**: `int`
- **spine_scenes**: `List[SpineSceneDesc]`
- **particlefxs**: `List[ParticleFXDesc]`
- **resources**: `List[ResourceDesc]`
- **materials**: `List[MaterialDesc]`
- **max_dynamic_textures**: `int`

### Enums:
- **AdjustReference**:
  - `ADJUST_REFERENCE_LEGACY = 0`
  - `ADJUST_REFERENCE_PARENT = 1`
  - `ADJUST_REFERENCE_DISABLED = 2`

---

## Message: `ScriptMessage`

### Fields:
- **descriptor_hash**: `int`
- **payload_size**: `int`
- **function**: `int`
- **unref_function**: `bool`

---

## Message: `ScriptUnrefMessage`

### Fields:
- **reference**: `int`

---

## Message: `SetCamera`

### Fields:
- **aspect_ratio**: `float`
- **fov**: `float`
- **near_z**: `float`
- **far_z**: `float`
- **orthographic_projection**: `int`
- **orthographic_zoom**: `float`
- **orthographic_mode**: `int`

---

## Message: `SetConstant`

### Fields:
- **name_hash**: `int`
- **value**: `Vector4`
- **index**: `int`

---

## Message: `SetConstantParticleFX`

### Fields:
- **emitter_id**: `int`
- **name_hash**: `int`
- **value**: `Matrix4`
- **is_matrix4**: `bool`

---

## Message: `SetConstantTileMap`

### Fields:
- **name_hash**: `int`
- **value**: `Vector4`

---

## Message: `SetFlipHorizontal`

### Fields:
- **flip**: `int`

---

## Message: `SetFlipVertical`

### Fields:
- **flip**: `int`

---

## Message: `SetGain`

### Fields:
- **gain**: `float`

---

## Message: `SetGridShapeHull`

### Fields:
- **shape**: `int`
- **row**: `int`
- **column**: `int`
- **hull**: `int`
- **flip_horizontal**: `int`
- **flip_vertical**: `int`
- **rotate90**: `int`

---

## Message: `SetLight`

### Fields:
- **position**: `Point3`
- **rotation**: `Quat`
- **light**: `LightDesc`

---

## Message: `SetPan`

### Fields:
- **pan**: `float`

---

## Message: `SetParent`

### Fields:
- **parent_id**: `int`
- **keep_world_transform**: `int`

---

## Message: `SetScale`

### Fields:
- **scale**: `Vector3`

---

## Message: `SetSpeed`

### Fields:
- **speed**: `float`

---

## Message: `SetText`

### Fields:
- **text**: `str`

---

## Message: `SetTexture`

### Fields:
- **texture_hash**: `int`
- **texture_unit**: `int`

---

## Message: `SetTimeStep`

### Fields:
- **factor**: `float`
- **mode**: `int`

---

## Message: `SetUpdateFrequency`

### Fields:
- **frequency**: `int`

---

## Message: `SetViewProjection`

### Fields:
- **id**: `int`
- **view**: `Matrix4`
- **projection**: `Matrix4`

---

## Message: `SetVsync`

### Fields:
- **swap_interval**: `int`

---

## Message: `ShaderDesc`

### Fields:
- **shaders**: `List[Shader]`
- **reflection**: `ShaderReflection`

### Enums:
- **Language**:
  - `LANGUAGE_GLSL_SM120 = 1`
  - `LANGUAGE_GLES_SM100 = 2`
  - `LANGUAGE_GLES_SM300 = 3`
  - `LANGUAGE_SPIRV = 4`
  - `LANGUAGE_PSSL = 5`
  - `LANGUAGE_GLSL_SM430 = 6`
  - `LANGUAGE_GLSL_SM330 = 7`
  - `LANGUAGE_WGSL = 8`
  - `LANGUAGE_HLSL_50 = 9`
  - `LANGUAGE_HLSL_51 = 10`
- **ShaderType**:
  - `SHADER_TYPE_VERTEX = 0`
  - `SHADER_TYPE_FRAGMENT = 1`
  - `SHADER_TYPE_COMPUTE = 2`
- **ShaderDataType**:
  - `SHADER_TYPE_UNKNOWN = 0`
  - `SHADER_TYPE_INT = 1`
  - `SHADER_TYPE_UINT = 2`
  - `SHADER_TYPE_FLOAT = 3`
  - `SHADER_TYPE_VEC2 = 4`
  - `SHADER_TYPE_VEC3 = 5`
  - `SHADER_TYPE_VEC4 = 6`
  - `SHADER_TYPE_MAT2 = 7`
  - `SHADER_TYPE_MAT3 = 8`
  - `SHADER_TYPE_MAT4 = 9`
  - `SHADER_TYPE_SAMPLER2D = 10`
  - `SHADER_TYPE_SAMPLER3D = 11`
  - `SHADER_TYPE_SAMPLER_CUBE = 12`
  - `SHADER_TYPE_SAMPLER2D_ARRAY = 13`
  - `SHADER_TYPE_UNIFORM_BUFFER = 14`
  - `SHADER_TYPE_UVEC2 = 15`
  - `SHADER_TYPE_UVEC3 = 16`
  - `SHADER_TYPE_UVEC4 = 17`
  - `SHADER_TYPE_TEXTURE2D = 18`
  - `SHADER_TYPE_UTEXTURE2D = 19`
  - `SHADER_TYPE_RENDER_PASS_INPUT = 20`
  - `SHADER_TYPE_UIMAGE2D = 21`
  - `SHADER_TYPE_IMAGE2D = 22`
  - `SHADER_TYPE_SAMPLER = 23`
  - `SHADER_TYPE_STORAGE_BUFFER = 24`
  - `SHADER_TYPE_TEXTURE2D_ARRAY = 25`
  - `SHADER_TYPE_TEXTURE_CUBE = 26`
  - `SHADER_TYPE_TEXTURE3D = 27`
  - `SHADER_TYPE_UTEXTURE3D = 28`
  - `SHADER_TYPE_UIMAGE3D = 29`
  - `SHADER_TYPE_IMAGE3D = 30`
  - `SHADER_TYPE_SAMPLER3D_ARRAY = 31`
  - `SHADER_TYPE_TEXTURE3D_ARRAY = 32`

---

## Message: `SoundDesc`

### Fields:
- **sound**: `str`
- **looping**: `int`
- **group**: `str`
- **gain**: `float`
- **pan**: `float`
- **speed**: `float`
- **loopcount**: `int`

---

## Message: `SoundEvent`

### Fields:
- **play_id**: `int`

---

## Message: `SpriteDesc`

### Fields:
- **tile_set**: `str`
- **default_animation**: `str`
- **material**: `str`
- **blend_mode**: `int`
- **slice9**: `Vector4`
- **size**: `Vector4`
- **size_mode**: `int`
- **offset**: `float`
- **playback_rate**: `float`
- **attributes**: `List[VertexAttribute]`
- **textures**: `List[SpriteTexture]`

### Enums:
- **BlendMode**:
  - `BLEND_MODE_ALPHA = 0`
  - `BLEND_MODE_ADD = 1`
  - `BLEND_MODE_ADD_ALPHA = 2`
  - `BLEND_MODE_MULT = 3`
  - `BLEND_MODE_SCREEN = 4`
- **SizeMode**:
  - `SIZE_MODE_MANUAL = 0`
  - `SIZE_MODE_AUTO = 1`

---

## Message: `SpriteGeometry`

### Fields:
- **width**: `int`
- **height**: `int`
- **center_x**: `float`
- **center_y**: `float`
- **rotated**: `bool`
- **trim_mode**: `int`
- **vertices**: `List[float]`
- **uvs**: `List[float]`
- **indices**: `List[int]`
- **pivot_x**: `float`
- **pivot_y**: `float`

---

## Message: `SpriteTexture`

### Fields:
- **sampler**: `str`
- **texture**: `str`

---

## Message: `StartRecord`

### Fields:
- **file_name**: `str`
- **frame_period**: `int`
- **fps**: `int`

---

## Message: `StopParticleFX`

### Fields:
- **clear_particles**: `bool`

---

## Message: `StopRecord`

_No fields_


---

## Message: `StopSound`

### Fields:
- **play_id**: `int`

---

## Message: `StreamDesc`

### Fields:
- **name**: `str`
- **value_type**: `int`
- **value_count**: `int`
- **ui**: `List[int]`
- **i**: `List[int]`
- **ui64**: `List[int]`
- **i64**: `List[int]`
- **f**: `List[float]`
- **name_hash**: `int`

---

## Message: `Texture`

### Fields:
- **sampler**: `str`
- **texture**: `str`

---

## Message: `TextureFormatAlternative`

### Fields:
- **format**: `int`
- **compression_level**: `int`
- **compression_type**: `int`
- **compressor**: `str`
- **compressor_preset**: `str`

### Enums:
- **CompressionLevel**:
  - `FAST = 0`
  - `NORMAL = 1`
  - `HIGH = 2`
  - `BEST = 3`

---

## Message: `TextureImage`

### Fields:
- **alternatives**: `List[Image]`
- **type**: `int`
- **count**: `int`
- **usage_flags**: `int`
- **image_data_address**: `int`

### Enums:
- **Type**:
  - `TYPE_2D = 1`
  - `TYPE_CUBEMAP = 2`
  - `TYPE_2D_ARRAY = 3`
  - `TYPE_2D_IMAGE = 4`
  - `TYPE_3D = 5`
  - `TYPE_3D_IMAGE = 6`
- **CompressionType**:
  - `COMPRESSION_TYPE_DEFAULT = 0`
  - `COMPRESSION_TYPE_WEBP = 1`
  - `COMPRESSION_TYPE_WEBP_LOSSY = 2`
  - `COMPRESSION_TYPE_BASIS_UASTC = 3`
  - `COMPRESSION_TYPE_BASIS_ETC1S = 4`
  - `COMPRESSION_TYPE_ASTC = 5`
- **CompressionFlags**:
  - `COMPRESSION_FLAG_ALPHA_CLEAN = 1`
- **TextureFormat**:
  - `TEXTURE_FORMAT_LUMINANCE = 0`
  - `TEXTURE_FORMAT_RGB = 1`
  - `TEXTURE_FORMAT_RGBA = 2`
  - `TEXTURE_FORMAT_RGB_PVRTC_2BPPV1 = 3`
  - `TEXTURE_FORMAT_RGB_PVRTC_4BPPV1 = 4`
  - `TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1 = 5`
  - `TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1 = 6`
  - `TEXTURE_FORMAT_RGB_ETC1 = 7`
  - `TEXTURE_FORMAT_RGB_16BPP = 8`
  - `TEXTURE_FORMAT_RGBA_16BPP = 9`
  - `TEXTURE_FORMAT_LUMINANCE_ALPHA = 10`
  - `TEXTURE_FORMAT_RGBA_ETC2 = 11`
  - `TEXTURE_FORMAT_RGBA_ASTC_4X4 = 12`
  - `TEXTURE_FORMAT_RGBA_ASTC_4x4 = 12`
  - `TEXTURE_FORMAT_RGB_BC1 = 13`
  - `TEXTURE_FORMAT_RGBA_BC3 = 14`
  - `TEXTURE_FORMAT_R_BC4 = 15`
  - `TEXTURE_FORMAT_RG_BC5 = 16`
  - `TEXTURE_FORMAT_RGBA_BC7 = 17`
  - `TEXTURE_FORMAT_RGB16F = 18`
  - `TEXTURE_FORMAT_RGB32F = 19`
  - `TEXTURE_FORMAT_RGBA16F = 20`
  - `TEXTURE_FORMAT_RGBA32F = 21`
  - `TEXTURE_FORMAT_R16F = 22`
  - `TEXTURE_FORMAT_RG16F = 23`
  - `TEXTURE_FORMAT_R32F = 24`
  - `TEXTURE_FORMAT_RG32F = 25`
  - `TEXTURE_FORMAT_RGBA_ASTC_5X4 = 26`
  - `TEXTURE_FORMAT_RGBA_ASTC_5X5 = 27`
  - `TEXTURE_FORMAT_RGBA_ASTC_6X5 = 28`
  - `TEXTURE_FORMAT_RGBA_ASTC_6X6 = 29`
  - `TEXTURE_FORMAT_RGBA_ASTC_8X5 = 30`
  - `TEXTURE_FORMAT_RGBA_ASTC_8X6 = 31`
  - `TEXTURE_FORMAT_RGBA_ASTC_8X8 = 32`
  - `TEXTURE_FORMAT_RGBA_ASTC_10X5 = 33`
  - `TEXTURE_FORMAT_RGBA_ASTC_10X6 = 34`
  - `TEXTURE_FORMAT_RGBA_ASTC_10X8 = 35`
  - `TEXTURE_FORMAT_RGBA_ASTC_10X10 = 36`
  - `TEXTURE_FORMAT_RGBA_ASTC_12X10 = 37`
  - `TEXTURE_FORMAT_RGBA_ASTC_12X12 = 38`

---

## Message: `TextureProfile`

### Fields:
- **name**: `str`
- **platforms**: `List[PlatformProfile]`

---

## Message: `TextureProfiles`

### Fields:
- **path_settings**: `List[PathSettings]`
- **profiles**: `List[TextureProfile]`

---

## Message: `TextureSet`

### Fields:
- **texture**: `str`
- **width**: `int`
- **height**: `int`
- **texture_hash**: `int`
- **animations**: `List[TextureSetAnimation]`
- **tile_width**: `int`
- **tile_height**: `int`
- **tile_count**: `int`
- **collision_hull_points**: `List[float]`
- **collision_groups**: `List[str]`
- **convex_hulls**: `List[ConvexHull]`
- **image_name_hashes**: `List[int]`
- **frame_indices**: `List[int]`
- **tex_coords**: `bytes`
- **tex_dims**: `bytes`
- **geometries**: `List[SpriteGeometry]`
- **use_geometries**: `int`
- **page_indices**: `List[int]`
- **page_count**: `int`

---

## Message: `TextureSetAnimation`

### Fields:
- **id**: `str`
- **width**: `int`
- **height**: `int`
- **start**: `int`
- **end**: `int`
- **fps**: `int`
- **playback**: `int`
- **flip_horizontal**: `int`
- **flip_vertical**: `int`

---

## Message: `TileCell`

### Fields:
- **x**: `int`
- **y**: `int`
- **tile**: `int`
- **h_flip**: `int`
- **v_flip**: `int`
- **rotate90**: `int`

---

## Message: `TileGrid`

### Fields:
- **tile_set**: `str`
- **layers**: `List[TileLayer]`
- **material**: `str`
- **blend_mode**: `int`

### Enums:
- **BlendMode**:
  - `BLEND_MODE_ALPHA = 0`
  - `BLEND_MODE_ADD = 1`
  - `BLEND_MODE_ADD_ALPHA = 2`
  - `BLEND_MODE_MULT = 3`
  - `BLEND_MODE_SCREEN = 4`

---

## Message: `TileLayer`

### Fields:
- **id**: `str`
- **z**: `float`
- **is_visible**: `int`
- **id_hash**: `int`
- **cell**: `List[TileCell]`

---

## Message: `TileSet`

### Fields:
- **image**: `str`
- **tile_width**: `int`
- **tile_height**: `int`
- **tile_margin**: `int`
- **tile_spacing**: `int`
- **collision**: `str`
- **material_tag**: `str`
- **convex_hulls**: `List[ConvexHull]`
- **convex_hull_points**: `List[float]`
- **collision_groups**: `List[str]`
- **animations**: `List[Animation]`
- **extrude_borders**: `int`
- **inner_padding**: `int`
- **sprite_trim_mode**: `int`

---

## Message: `TogglePhysicsDebug`

_No fields_


---

## Message: `ToggleProfile`

_No fields_


---

## Message: `Transform`

### Fields:
- **rotation**: `Quat`
- **translation**: `Vector3`
- **scale**: `Vector3`

---

## Message: `Trigger`

### Fields:
- **id**: `int`
- **group**: `int`

---

## Message: `TriggerEvent`

### Fields:
- **enter**: `bool`
- **a**: `Trigger`
- **b**: `Trigger`

---

## Message: `TriggerResponse`

### Fields:
- **other_id**: `int`
- **enter**: `bool`
- **group**: `int`
- **other_group**: `int`
- **own_group**: `int`

---

## Message: `Vector3`

### Fields:
- **x**: `float`
- **y**: `float`
- **z**: `float`
- **d**: `float`

---

## Message: `Vector3One`

### Fields:
- **x**: `float`
- **y**: `float`
- **z**: `float`
- **d**: `float`

---

## Message: `Vector4`

### Fields:
- **x**: `float`
- **y**: `float`
- **z**: `float`
- **w**: `float`

---

## Message: `Vector4One`

### Fields:
- **x**: `float`
- **y**: `float`
- **z**: `float`
- **w**: `float`

---

## Message: `Vector4WOne`

### Fields:
- **x**: `float`
- **y**: `float`
- **z**: `float`
- **w**: `float`

---

## Message: `VelocityResponse`

### Fields:
- **linear_velocity**: `Vector3`
- **angular_velocity**: `Vector3`

---

## Message: `VertexAttribute`

### Fields:
- **name**: `str`
- **name_hash**: `int`
- **semantic_type**: `int`
- **element_count**: `int`
- **normalize**: `bool`
- **data_type**: `int`
- **coordinate_space**: `int`
- **step_function**: `int`
- **vector_type**: `int`
- **long_values**: `LongValues`
- **double_values**: `DoubleValues`
- **binary_values**: `bytes`

### Enums:
- **DataType**:
  - `TYPE_BYTE = 1`
  - `TYPE_UNSIGNED_BYTE = 2`
  - `TYPE_SHORT = 3`
  - `TYPE_UNSIGNED_SHORT = 4`
  - `TYPE_INT = 5`
  - `TYPE_UNSIGNED_INT = 6`
  - `TYPE_FLOAT = 7`
- **VectorType**:
  - `VECTOR_TYPE_SCALAR = 1`
  - `VECTOR_TYPE_VEC2 = 2`
  - `VECTOR_TYPE_VEC3 = 3`
  - `VECTOR_TYPE_VEC4 = 4`
  - `VECTOR_TYPE_MAT2 = 5`
  - `VECTOR_TYPE_MAT3 = 6`
  - `VECTOR_TYPE_MAT4 = 7`
- **SemanticType**:
  - `SEMANTIC_TYPE_NONE = 1`
  - `SEMANTIC_TYPE_POSITION = 2`
  - `SEMANTIC_TYPE_TEXCOORD = 3`
  - `SEMANTIC_TYPE_PAGE_INDEX = 4`
  - `SEMANTIC_TYPE_COLOR = 5`
  - `SEMANTIC_TYPE_NORMAL = 6`
  - `SEMANTIC_TYPE_TANGENT = 7`
  - `SEMANTIC_TYPE_WORLD_MATRIX = 8`
  - `SEMANTIC_TYPE_NORMAL_MATRIX = 9`
  - `SEMANTIC_TYPE_BONE_WEIGHTS = 10`
  - `SEMANTIC_TYPE_BONE_INDICES = 11`

---

## Message: `WindowResized`

### Fields:
- **width**: `int`
- **height**: `int`

---

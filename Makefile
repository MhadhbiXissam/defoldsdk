


.PHONY : onstartup clean build

onstartup : 
	. .vscode/scripts.sh && onstartup

clean : 
	. .vscode/scripts.sh && clean

build : 
	. .vscode/scripts.sh && build

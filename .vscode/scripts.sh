set -e 

onstartup() {
    if [ -d ".venv" ]; then
        echo ".venv exists"
        .venv/bin/pip install -r requirements.txt
    else
        echo ".venv not found"
        python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

    fi
}




clean(){
    if [ -d "dist" ]; then rm -rf dist 
    fi
    if [ -d "defoldsdk.egg-info" ]; then 
        rm -rf defoldsdk.egg-info 
    fi
    if [ -d "build" ]; then 
        rm -rf build 
    fi
}

build(){
    python -m build
    twine upload dist/* -u __token__ -p $PYPI_TOKEN

}
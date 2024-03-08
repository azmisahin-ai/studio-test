#!/bin/sh

# test launch commands.
echo TEST
echo APP_ENV=$APP_ENV
echo APP_NAME=$APP_NAME
echo DISTRIB_ID=$DISTRIB_ID
echo WORKSPACE_FOLDER=$WORKSPACE_FOLDER
echo PROJECT_FOLDER=$PROJECT_FOLDER
echo DATA_FOLDER=$DATA_FOLDER
echo RESOURCE_CPUS=$RESOURCE_CPUS
echo RESOURCE_GPUS=$RESOURCE_GPUS
echo RESOURCE_MEMORY=$RESOURCE_MEMORY
echo SCALE=$SCALE
echo HOST_IP=$HOST_IP
echo TCP_PORT=$TCP_PORT
echo TCP_RANGE=$TCP_RANGE
echo SWICH_TRACKING_TRACE=$SWICH_TRACKING_TRACE
echo SWICH_TRACKING_DEBUG=$SWICH_TRACKING_DEBUG
echo SWICH_TRACKING_INFO=$SWICH_TRACKING_INFO
echo SWICH_TRACKING_WARN=$SWICH_TRACKING_WARN
echo SWICH_TRACKING_ERROR=$SWICH_TRACKING_ERROR
echo SWICH_TRACKING_VERBOSE=$SWICH_TRACKING_VERBOSE
echo SWICH_TRACKING_REPORT=$SWICH_TRACKING_REPORT
echo PYTHONPATH=$PYTHONPATH

echo ==========

. $DATA_FOLDER/.venv/bin/activate
if [ $? -ne 0 ]; then
  echo "✖️ Failed to activate virtual environment."
  exit 1
else
  echo "✅ Virtual environment activated."
fi

black .
if [ $? -ne 0 ]; then
  echo "✖️ Automatically formatting Python code failed."
  exit 1
else
  echo "✅ Automatically formatting Python code succeeded."
fi

flake8
if [ $? -ne 0 ]; then
  echo "✖️ Linting errors found. Please fix them before committing."
  exit 1
else
  echo "✅ Linting passed."
fi

sphinx-apidoc -o /workspaces/template/dist/docs  /workspaces/template/src
if [ $? -ne 0 ]; then
  echo "✖️ Documentation generation code failed."
  exit 1
else
  echo "✅ Automatically the Documentation code was successful."
fi

behave
if [ $? -ne 0 ]; then
  echo "✖️ Behavior-driven development failed."
  exit 1
else
  echo "✅ Behavior-driven development was successful."
fi

$DATA_FOLDER/.venv/bin/gunicorn --bind $HOST_IP:$TCP_PORT "src.web.app:app"
if [ $? -ne 0 ]; then
  echo "✖️ Package failed."
  exit 1
else
  echo "✅ Package was successful."
fi

echo ==========

sleep infinity

/bin/sh

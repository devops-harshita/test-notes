#!/bin/bash

# Define variables
LAYER_NAME="jinja_layer"
LAYER_DIR="$LAYER_NAME/python"
ZIP_FILE="$LAYER_NAME.zip"

# Create the layer directory structure
mkdir -p $LAYER_DIR

# Install Jinja2 into the layer directory
pip install jinja2 -t $LAYER_DIR/

# Zip the layer
cd $LAYER_NAME
zip -r $ZIP_FILE python

# Move back to the original directory
cd ..

# Output the location of the zip file
echo "Layer zip created at: ./$LAYER_NAME/$ZIP_FILE"

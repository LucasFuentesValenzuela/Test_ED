#!/bin/bash
#This is to run Kiril's code with Kiril's document to see if it compiles properly

#AT='~/routing/Build/Devel/Launchers/./AssignTraffic'
AT='../../routing/routing-framework/Build/Devel/Launchers/./AssignTraffic'
FLAGS='-v -so -a ch -ord input'
NUM_ITER=0
DUMMY='-dummy 1351' #to be removed for elastic demand!
PARAMS='-eco 0.8 -f custom_bpr'

GRAPH_PATH='DocKiril/graph.gr.bin'
OD_PATH='DocKiril/od.csv'
OUTPUT_PATH='DocKiril/output/output'
FLOW_PATH='DocKiril/flow/flow'

$AT $FLAGS -n $NUM_ITER $DUMMY $PARAMS -i $GRAPH_PATH -od $OD_PATH -o $OUTPUT_PATH -fp $FLOW_PATH

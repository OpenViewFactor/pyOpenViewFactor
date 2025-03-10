import subprocess

#! ---------- GLOBAL FUNCTION FOR EXECUTING THE OVF SOLVER ---------- !#
def RunOVF(HELP = False,
           OVF_EXE_PATH = None,
           inputs = None,
           obstructions = None,
           selfint = None,
           numerics = None,
           compute = None,
           precision = None,
           backfacecull = None,
           blockingtype = None,
           matrixout = "NONE",
           graphicout = "NONE",
           bvhout = "NONE",
           logfile = "NONE"):
  
  command_line_arguments = [
    OVF_EXE_PATH
  ]

  if HELP:
    print('<-----> Python Interface Options <----->')
    print('HELP\t\t\t<--> (= False/True) Prints out this help window.')
    print('OVF_EXE_PATH\t\t<--> Pass the absolute / relative filepath of the openviewfactor binary as a string.')
    print('inputs\t\t\t<--> Pass the absolute / relative filepath(s) for 1 or 2 input meshes in the .stl format. Use a list of strings for 2.')
    print('obstructions\t\t<--> Pass the absolute / relative filepath(s) for any obstructive meshes in the .stl format. Use a list of strings for more than one.')
    print('blockingtype\t\t<--> (= "BVH"/"NAIVE") Determines whether to apply blocking using naive moller-trumbore intersection or to utilize the Boundary Volume Hierarchy.')
    print('selfint\t\t\t<--> (= "NONE"/"BOTH"/"EMITTER"/"RECEIVER") Determines which of the input meshes should be treated as potential obstructive meshes.')
    print('backfacecull\t\t<--> (= "ON"/"OFF") Determines whether the back-face culling algorithm will be applied to the two input meshes.')
    print('numerics\t\t<--> (= "DAI"/"SAI") Determines the numerical integration scheme used.')
    print('compute\t\t\t<--> (= "CPU_N"/"GPU"/"GPU_N") Determines the compute back-end.')
    print('precision\t\t<--> (= "DOUBLE"/"SINGLE") Determines the floating-point precision.')
    print('matrixout\t\t<--> (= "NONE") Pass the absolute / relative filepath to write the sparse output matrix.')
    print('graphicout\t\t<--> (= "NONE") Pass the absolute / relative filepath to write the graphic file. Use a list of strings to separate each mesh into unique visualizations.')
    print('bvhout\t\t\t<--> (= "NONE") Pass the absolute / relative file path to write the Boundary Volume Hierarchy for the blocking structure.')
    print('logfile\t\t\t<--> (= "NONE") Pass the absolute / relative file path to write the solver command-line output to a log file.')

    if not(OVF_EXE_PATH == None):
      command_line_arguments.extend(['-h'])
      print('<-----> Core OpenViewFactor CLI <----->')
      completed_process = subprocess.run(command_line_arguments)
      return completed_process
    return

  if inputs == None:
    print('You must provide at least one input mesh.')
    print('For a reminder on the core command-line interface, pass "HELP_TOGGLE = True" to this function')
    return

  #* ----- LOAD INPUT MESHES ----- *#
  command_line_arguments.extend(['-i'])
  if not(isinstance(inputs, list)):
    command_line_arguments.extend([inputs])
  else:
    command_line_arguments.extend([mesh for mesh in inputs])

  #* ----- LOAD BLOCKING MESHES ----- *#
  if not(obstructions == None):
    command_line_arguments.extend(['-o'])
    if not(isinstance(obstructions,list)):
      command_line_arguments.extend([obstructions])
    else:
      command_line_arguments.extend([mesh for mesh in obstructions])

  #* ----- LOAD OTHER OPTIONS ----- *#
  command_line_arguments.extend(['-s', selfint])
  command_line_arguments.extend(['-n', numerics])
  command_line_arguments.extend(['-c', compute])
  command_line_arguments.extend(['-p', precision])
  command_line_arguments.extend(['-m', matrixout])
  command_line_arguments.extend(['-g', graphicout])
  command_line_arguments.extend(['-b', bvhout])
  command_line_arguments.extend(['-f', backfacecull])
  command_line_arguments.extend(['-t', blockingtype])
  command_line_arguments.extend(['-l', logfile])

  subprocess.run(command_line_arguments)

if __name__ == "__main__":
  RunOVF(HELP=True)
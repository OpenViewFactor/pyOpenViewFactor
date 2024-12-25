import subprocess

#! ---------- GLOBAL FUNCTION FOR EXECUTING THE OVF SOLVER ---------- !#
def RunOVF(OVF_EXE_PATH : str = None,
           HELP_TOGGLE : bool = False,
           INPUT_MESHES : str = None,
           BLOCKING_MESHES : str = None,
           INTERSECTION_OPTION : str = 'NONE',
           NUMERICAL_METHOD : str = 'DAI',
           COMPUTE_OPTION : str = 'CPU_N',
           PRECISION : str = 'DOUBLE',
           PLAINTEXT_OUTPUT_PATH : str = 'NONE',
           GRAPHIC_OUTPUT_PATH : str = 'NONE'):
  
  command_line_arguments = [
    OVF_EXE_PATH
  ]

  if HELP_TOGGLE:
    print('<-----> Python Interface Options <----->')
    print('OVF_EXE_PATH\t\t<--> Pass the absolute / relative filepath of the openviewfactor binary as a string.')
    print('HELP_TOGGLE\t\t<--> (= False/True) Prints out this help window.')
    print('INPUT_MESHES\t\t<--> Pass the absolute / relative filepath(s) for 1 or 2 input meshes in the .stl format. Use a list of strings for 2.')
    print('BLOCKING_MESHES\t\t<--> Pass the absolute / relative filepath(s) for any obstructive meshes in the .stl format. Use a list of strings for more than one.')
    print('INTERSECTION_OPTION\t<--> (= "NONE"/"BOTH"/"EMITTER"/"RECEIVER") Determines which of the input meshes should be treated as potential obstructive meshes.')
    print('NUMERICAL_METHOD\t<--> (= "DAI") Determines the numerical integration scheme used.')
    print('COMPUTE_OPTION\t\t<--> (= "CPU_N"/"CPU"/"GPU"/"GPU_N") Determines the compute back-end.')
    print('PRECISION\t\t<--> (= "DOUBLE"/"SINGLE") Determines the floating-point precision.')
    print('PLAINTEXT_OUTPUT_PATH\t<--> (= "NONE") Pass the absolute / relative filepath to write the sparse output matrix.')
    print('GRAPHIC_OUTPUT_PATH\t<--> (= "NONE") Pass the absolute / relative filepath to write the graphic file. Use a list of strings to separate each mesh into unique visualizations.')
    if not(OVF_EXE_PATH == None):
      command_line_arguments.extend(['-h'])
      print('<-----> Core OpenViewFactor CLI <----->')
      completed_process = subprocess.run(command_line_arguments)
      return completed_process
    return

  if INPUT_MESHES == None:
    print('You must provide at least one input mesh.')
    print('For a reminder on the core command-line interface, pass "HELP_TOGGLE = True" to this function')
    return

  #* ----- LOAD INPUT MESHES ----- *#
  command_line_arguments.extend(['-i'])
  if not(isinstance(INPUT_MESHES, list)):
    command_line_arguments.extend([INPUT_MESHES])
  else:
    command_line_arguments.extend([mesh for mesh in INPUT_MESHES])

  #* ----- LOAD BLOCKING MESHES ----- *#
  if not(BLOCKING_MESHES == None):
    command_line_arguments.extend(['-b'])
    if not(isinstance(BLOCKING_MESHES,list)):
      command_line_arguments.extend([BLOCKING_MESHES])
    else:
      command_line_arguments.extend([mesh for mesh in BLOCKING_MESHES])

  #* ----- LOAD OTHER OPTIONS ----- *#
  command_line_arguments.extend(['-s', INTERSECTION_OPTION])
  command_line_arguments.extend(['-n', NUMERICAL_METHOD])
  command_line_arguments.extend(['-c', COMPUTE_OPTION])
  command_line_arguments.extend(['-p', PRECISION])
  command_line_arguments.extend(['-o', PLAINTEXT_OUTPUT_PATH])
  command_line_arguments.extend(['-g', GRAPHIC_OUTPUT_PATH])

  completed_process = subprocess.run(command_line_arguments, stdout = subprocess.PIPE, text = True)

  return completed_process

if __name__ == "__main__":
  RunOVF(HELP_TOGGLE=True)
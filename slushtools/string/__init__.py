# Slush Tools STRING Module

class String:
  bu = None
  dat = None
  def __init__(str):
    if str == None:
      print("String argument required.")
      exit()
    else:
      dat = str
      bu = str
      return dat
  def reset():
    dat = bu
    return dat
  def format(type="custom",args={}):
    if type == "custom":
      for i,v in args:
        x = dat.split("$" + i)
        v.join(v)
      dat = x
      return dat
    elif type == "py":
      x = dat.format(*args)
      dat = x
      return dat
    else:
      print("Unknown format type.")
    def append(str):
      dat = dat + str
      return dat
    def endswith(str):
      if dat[len(dat)-len(str):len(str)] == str:
        return True
      else:
        return False
    def simple(delimiter):
      return dat.split(delimiter)

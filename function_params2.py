def print_msg(msg,error="No Error", *kwargs):
   print("Log: "+error+" : "+msg)
   print(kwargs)

print_msg("This will be logged","File Not Found","1","2","3","4","5","6","6")


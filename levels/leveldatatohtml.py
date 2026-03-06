print("Make sure you loaded the right level data!")
# Put the level data after "data=", the rest will be requested with input()
data={'level':[
  "00000000000000000000000000000000",
  "00000000000000000000000000000000",
  "00000000000000000000000000000000",
  "11110000000000000000000001111111",
  "00100000004304000400300400100000",
  "01000400000200000000200000010000",
  "10000000000200000000200000001000",
  "00000000000200000003230400000100",
  "00000000000200000002220000000010",
  "00000000000200000002220000000001",
  "00000000400200400002220000000000",
  "00000000000400000002220000111111",
  "11111100000000000002224000010000",
  "00001000000000000000000000001000",
  "00010000000000000444004444000100",
  "00100000000000000000000000000010"],
  'sp':[2,11],
  'ep':[1,2],
  'cols':[(150,200,255),(173,87,1),(42,67,187),(0,255,225)]}
#...
ratetype="-1"
ratetypes=[""," ☁"," ✿"]
levelname=input("Name of level: ")
authorname=input("Name of author: ")
while ratetype not in ["0","1","2"]:ratetype=input("Rate type (none: 0, cloud: 1, flower: 2): ")
imagepath=input("Path to image (e. g. example.png): ")
print("\n<!DOCTYPE html>\n<html>\n<head>\n\t<link rel=\"stylesheet\" type=\"text/css\" href=\"../style.css\">\n\t<style>\n\t\t.dropdown {\n\t\t\tposition: relative;\n\t\t\tpadding: 20px 30px;\n\t\t\tborder-radius: 4px;\n\t\t\tbackground-color: #000;\n\t\t\tcolor: #FFF;\n\t\t\tdisplay: inline-block;\n\t\t}\n\t\t.dropdown-content {\n\t\t\tdisplay: none;\n\t\t\tposition: absolute;\n\t\t\tcolor: #000;\n\t\t\tbackground-color: #f9f9f9;\n\t\t\tborder-radius: 4px;\n\t\t\tmin-width: 550px;\n\t\t\tbox-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);\n\t\t\tpadding: 12px 16px;\n\t\t\tfont-size: 16px;\n\t\t}\n\t\t.dropdown:hover .dropdown-content {\n\t\t\tdisplay: block;\n\t\t}\n\t</style>\n</head>\n<body><article style=\"padding-top: 0;\">\n\t<h3>",levelname," by ",authorname,ratetypes[int(ratetype)],"</h3><br>\n\t<img src=\"level images/",imagepath,"\"><br><br>\n\t<div class=\"-= dropdown\">Data (hover to view)\n\t<div class=\"dropdown-content\">{'level':[<br>",sep="")
for l in data['level']:print("\t&nbsp;&nbsp;\"",l,"\",<br>",sep="")
print("\t&nbsp;&nbsp;'sp':[",data['sp'][0],",",data['sp'][1],"],<br>\n\t&nbsp;&nbsp;'ep':[",data['ep'][0],",",data['ep'][1],"],<br>\n\t&nbsp;&nbsp;'cols':","".join("("+str(data['cols'][n][0])+","+str(data['cols'][n][1])+","+str(data['cols'][n][2])+")" for n in range(4)),"}</div></div>\n</article></body>\n</html>",sep="")

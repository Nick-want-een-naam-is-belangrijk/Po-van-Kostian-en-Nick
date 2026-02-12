print("Make sure you loaded the right level data!")
# Put the level data after "data=", the rest will be requested with input()
data={'level':[
  "00000000000004443444444342111111",
  "00121212000344444444344442111111",
  "02000000144444344430000442111222",
  "01000000244444440000000040222000",
  "02000210144330000000000040000000",
  "00121334421443000000000040000000",
  "00030003434443000000000040000000",
  "00030000434303000000000040000000",
  "00020301324300000000000040000000",
  "00344434444300000000000040000000",
  "00034444233000000000000040000000",
  "00003313000000000000000444000022",
  "00000000000000000022224444422211",
  "00000000000000222211112444211111",
  "00000000000222111111111222111111",
  "00000000002111111111111111111111"],
  'sp':[3,4],
  'ep':[0,0],
  'cols':[(202,173,255),(77,117,83),(147,251,154),(255,0,75)]}
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

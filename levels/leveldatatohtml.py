print("Make sure you loaded the right level data!")
# Put the level data after "data=", the rest will be requested with input()
data={'level':[
  "11112004002111200000000021111111",
  "11112004002111200000000021122211",
  "11112003002111200000000021200021",
  "11112004002111230000000321200021",
  "11112004002222203000003422222021",
  "11112003000030004300034444443421",
  "11112004000000044433344244344421",
  "11112004000323444444442033132311",
  "11112003002111244444420021111111",
  "11222004002121244433300021111111",
  "12000004002111244400000021111111",
  "12000003002121243400000021111111",
  "11222004002111230400000021111111",
  "11112004002121200400000021111111",
  "11112044402111204440000021111111",
  "11112444442111244444444421111111"],
  'sp':[3,11],
  'ep':[27,3],
  'cols':[(170,170,255),(115,101,149),(235,224,255),(179,255,179)]}
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

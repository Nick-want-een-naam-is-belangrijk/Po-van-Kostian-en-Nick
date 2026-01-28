print("Make sure you loaded the right level data!")
# Put the level data after "data=", the rest will be requested with input()
data={'level':[
  "00021111111111111111111111111200",
  "00021111121112111111111111111200",
  "00021111111111111111111111112000",
  "00002111121212111111111111112000",
  "00002111122222111133111111120000",
  "00000233111111113300211323200000",
  "00000000311111130000313000300000",
  "00000000021111120000313000000000",
  "00000000021123120020323032230000",
  "00000233033300300030000021120000",
  "00002113000000020002002211112220",
  "00002113000000000030003111111112",
  "02221111323000320032331111111111",
  "21111111111233113311111111111111",
  "11111111111111111111111111111111",
  "11111111111111111111111111111111"],
  'sp':[2,11],
  'ep':[29,9],
  'cols':[(188,218,255),(105,105,187),(245,255,186),(157,255,143)]}
#...
ratetype="-1"
ratetypes=[""," ☁"," ✿"]
levelname=input("Name of level: ")
authorname=input("Name of author: ")
while ratetype not in ["0","1","2"]:ratetype=input("Rate type (none: 0, cloud: 1, flower: 2): ")
imagepath=input("Path to image (e. g. level images/example.png): ")
print("\n<!DOCTYPE html>\n<html>\n<head>\n\t<link rel=\"stylesheet\" type=\"text/css\" href=\"../style.css\">\n\t<style>\n\t\t.dropdown {\n\t\t\tposition: relative;\n\t\t\tpadding: 20px 30px;\n\t\t\tborder-radius: 4px;\n\t\t\tbackground-color: #000;\n\t\t\tcolor: #FFF;\n\t\t\tdisplay: inline-block;\n\t\t}\n\t\t.dropdown-content {\n\t\t\tdisplay: none;\n\t\t\tposition: absolute;\n\t\t\tcolor: #000;\n\t\t\tbackground-color: #f9f9f9;\n\t\t\tborder-radius: 4px;\n\t\t\tmin-width: 550px;\n\t\t\tbox-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);\n\t\t\tpadding: 12px 16px;\n\t\t\tfont-size: 16px;\n\t\t}\n\t\t.dropdown:hover .dropdown-content {\n\t\t\tdisplay: block;\n\t\t}\n\t</style\n</head>\n<body><article style=\"padding-top: 0;\">\n\t<h3>",levelname," by ",authorname,ratetypes[int(ratetype)],"</h3><br>\n\t<img src=\"",imagepath,"\"><br><br>\n\t<div class=\"-= dropdown\">Data (hover to view)\n\t<div class=\"dropdown-content\">{'level':[<br>",sep="")
for l in data['level']:print("\t&nbsp;&nbsp;\"",l,"\",<br>",sep="")
print("\t&nbsp;&nbsp;'sp':[",data['sp'][0],",",data['sp'][1],"],<br>\n\t&nbsp;&nbsp;'ep':[",data['ep'][0],",",data['ep'][1],"],<br>\n\t&nbsp;&nbsp;'cols':","".join("("+str(data['cols'][n][0])+","+str(data['cols'][n][1])+","+str(data['cols'][n][2])+")" for n in range(4)),"}</div></div>\n</article></body>\n</html>",sep="")

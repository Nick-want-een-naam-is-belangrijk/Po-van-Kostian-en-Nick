print("Make sure you loaded the right level data!")
# Put the level data after "data=", the rest will be requested with input()
data={'level':[
  "11111132311111111111111111111111",
  "11133344431332131111333111111111",
  "11200043432000303333000211111111",
  "11300043433020000000000311111111",
  "13003333444433232002330323132311",
  "11231133444431113031134440304431",
  "11113303333311130031134430003431",
  "11330000002111112332313333230031",
  "13000232031131323244434443000031",
  "13023113043303044443444240023311",
  "13030333030000034331323132332311",
  "13000003000232303313323244004031",
  "11323203323244000034444443003031",
  "11111300044443232004434330030031",
  "11111132434331111323313112312311",
  "11111111313111111111111111111111"],
  'sp':[2,4],
  'ep':[30,10],
  'cols':[(34,0,77),(0,0,0),(203,164,108),(161,194,112)]}
#...
ratetype="-1"
ratetypes=[""," ☁"," ✿"]
levelname=input("Name of level: ")
authorname=input("Name of author: ")
while ratetype not in ["0","1","2"]:ratetype=input("Rate type (none: 0, cloud: 1, flower: 2): ")
imagepath=input("Path to image (e. g. example.png): ")
print("\n<!DOCTYPE html>\n<html>\n<head>\n\t<link rel=\"stylesheet\" type=\"text/css\" href=\"../style.css\">\n\t<style>\n\t\t.dropdown {\n\t\t\tposition: relative;\n\t\t\tpadding: 20px 30px;\n\t\t\tborder-radius: 4px;\n\t\t\tbackground-color: #000;\n\t\t\tcolor: #FFF;\n\t\t\tdisplay: inline-block;\n\t\t}\n\t\t.dropdown-content {\n\t\t\tdisplay: none;\n\t\t\tposition: absolute;\n\t\t\tcolor: #000;\n\t\t\tbackground-color: #f9f9f9;\n\t\t\tborder-radius: 4px;\n\t\t\tmin-width: 550px;\n\t\t\tbox-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);\n\t\t\tpadding: 12px 16px;\n\t\t\tfont-size: 16px;\n\t\t}\n\t\t.dropdown:hover .dropdown-content {\n\t\t\tdisplay: block;\n\t\t}\n\t</style\n</head>\n<body><article style=\"padding-top: 0;\">\n\t<h3>",levelname," by ",authorname,ratetypes[int(ratetype)],"</h3><br>\n\t<img src=\"level images/",imagepath,"\"><br><br>\n\t<div class=\"-= dropdown\">Data (hover to view)\n\t<div class=\"dropdown-content\">{'level':[<br>",sep="")
for l in data['level']:print("\t&nbsp;&nbsp;\"",l,"\",<br>",sep="")
print("\t&nbsp;&nbsp;'sp':[",data['sp'][0],",",data['sp'][1],"],<br>\n\t&nbsp;&nbsp;'ep':[",data['ep'][0],",",data['ep'][1],"],<br>\n\t&nbsp;&nbsp;'cols':","".join("("+str(data['cols'][n][0])+","+str(data['cols'][n][1])+","+str(data['cols'][n][2])+")" for n in range(4)),"}</div></div>\n</article></body>\n</html>",sep="")

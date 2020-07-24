# <font size=6><br>_**gisd.py</br></font> <font size=4>(Google Image Searching and Downloading)**_</font>

## <font color=white>_Feature_</font>
<font size=4>Let's <font color=grean><b>_Search_</b></font> and <font color=yellow><b>_Save_</b> </font>google images with <font color=red><b>_Keywords_ </b></font>!!</font>

## Description
+ Imaging searching python script using Google Engine
+ The script is very simple to use and useful for many purpose
+ Outputs of the script are searched images and their original links
+ The script needs <b>_python3_</b> and <b>_Chrome_, _Safari_</b>
+ <font color=yellow>The script searches images from <b> _all scrolled pages_ </b></font>
+ _Progressbar_ is supporting in this version
![](assets/README-b414761f.png)

## Required Modules
+ sys  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` pip install sys```
+ os &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` pip install os```
+ argparse &nbsp;&nbsp;&nbsp;&nbsp;``` pip install argparse```
+ urllib3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` pip install urllib3```
+ requests &nbsp;&nbsp;&nbsp;&nbsp;``` pip install requests```
+ tqdm &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` pip install tqdm```
+ selenium &nbsp;&nbsp;&nbsp;&nbsp;``` pip install selenium```

## Usage
+ <b>Run in Terminal</b>
```
gisd.py Lottetower_편의점_지하철 8
gisd.py 롯데타워 8
gisd.py Lottetower,편의점,서울 8
```
+ <b>Help</b>
```
gisd.py --help
```

## Tips
+ If you want to search images with multiple keywords, just use <b> '_' </b> between keywords
+ If you want to separated image group with multiple keywords, just use <b> ',' </b> between keywords. This option will give you multiple grouped results.

## Outputs
* <font size=4>_Searched images in keyword named folder_</font>
![](assets/README-d40800d4.png)

* <font size=4>_Links  of the searched images_</font>
![](assets/README-95c20b9e.png)


## Version history
+ Version 0.1: the script release (2020.07.23)

## _Contact for Feedback and Bug Reports_
_Uksu, Choi (qtwing@naver.com)_

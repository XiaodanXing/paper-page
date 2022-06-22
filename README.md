# paper-page
A simple tool to create a new github page for your papers

If you would like to promote your paper by webpages like [this](phillipi.github.io/pix2pix/), and you don't know nothing about HTML formatting, then this resporitory is right for you!

Based on the format from [pix2pix](phillipi.github.io/pix2pix/), paper-page used a python file to convert the attributes from the [configuration file](./config.py) to an [HTML file](./docs/index.html). And this html file can be added directly to your github resporitories alongside with all your codes, and can be compiled into a webpage related to your paper!

Dependencies:
```
pip install pandas bs4 easydict
```

## Step 1. Create a HTML file
1. Clone this resporitory in your pc by
```
git clone https://github.com/XiaodanXing/paper-page.git
```

2. Edit the [configuration file](./config.py). Editable attributes include title, abstract, method and results. Please do not try to delete any major attributes. However, you can delete the number of items shown in your result section. You can also add new items by creating indexed results attributes.
```
__C.results.item5 = {}
__C.results.item5.title = 'Item 5'
__C.results.item5.filepath = './resources/item5.png'
__C.results.item5.caption = 'Item 5'
__C.results.item5.type = 'figure'
```

3. Generate the HTML file by running
```
python main.py
```
Then, you will find your HTML file in the docs folder, as well as all your images attached to the HTML. 


## Step 2. Generate a GitHub Page for your resporitory
1. Upload the docs folder directly into your resporitory.


2. Enable your page compiling in the setting of your resporitory.
![image](https://user-images.githubusercontent.com/30890745/175132576-762e9242-6066-45cd-ba2b-24271c688d09.png)

3. Select the docs folder as the folder for your page contents.
![image](https://user-images.githubusercontent.com/30890745/175132837-820600b7-0f4b-49ec-8d46-cabfd0b70891.png)

4. Wait 10-15min, then you can access your GitHub page by https://[your name].github.io/your git name/
![image](https://user-images.githubusercontent.com/30890745/175133179-29738f8a-6db6-48c5-8d9f-9e0ebcb4c642.png)


## Features to be implemented

Excel formatting

## Why should I use paper-page not Markdown?

[HTML vs Markdown](https://developers.google.com/style/markdown)


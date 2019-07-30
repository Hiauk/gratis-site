**Gratis site** is a current ongoing project.

## Get started

To begin with you will need to download the project files onto your PC. A simple way is to git clone it.

```
git clone https://github.com/Hiauk/gratis-site.git
```

## Create a page

Within the ```pages``` folder you need to create a new file called ```index```. This will act as the homepage for your new website.

```
cd pages
touch index
vim index
```

## Writing in a Gratis site page

I have tried to keep the formatting for content to a bare minimum at the moment, but this might be built upon in the future.

Currently the generator supports:

```
# H1 title
## H2 title
### H3 title
#### H4 title
##### H5 title

+ list item
+ next list item
+ final list item

And this would be formatted like a normal paragraph of text.
```

For each page you wish to have on your website just simply create another file within the ```pages``` folder.

Eg.

```
|gratis-site
|-css/
    |-kube.min.css
    |-main.css
|-ouput/
    |-server.py
|-pages/
    |-index
    |-about
    |-contact
|-parse.py
|-template.py
```

## Generate the website

Once you have made your pages generating the site is very simple.

```
python3 parse.py
```

This will turn all your ```pages/``` files into html using the ```template.py``` file.

## Run the server

I have included a barebones server for testing the output of the generator called ```server.py```. It is recommended that the site be run on [NGINX](https://www.nginx.com) or [Apache](https://www.apache.org) if used within a production environment.

```
cd output/
python3 server.py
```

And then navigate to [http://localhost:8080](http://localhost:8080) to see the website.

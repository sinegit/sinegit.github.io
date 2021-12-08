Note: This page was built using the template provided by the folks from the [Kording Lab](https://kordinglab.com/). Thanks!

# SINE lab page

This is the repository for [SINE lab page](https://sinegit.github.io/). We use Jekyll to run our Github page. We are welcome for other people to contribute to our site not just lab members. Feel free to fork and pull-request!

## Workflow

### Maintaining the `sources` branch

1. Clone the `sources` branch of this repository
```bash
git clone -b sources https://github.com/sinegit/sinegit.github.io.git
```
2. Install the dependencies specified in the Gemfile
```bash
bundle install
```
3. Build the website
```bash
bundle exec jekyll build
```
This will create the destination directory `_site/` and build the site into it.

4. Add file contents to the index
```bash
git add -A
```
5. Commit the changes
```bash
git commit -m "Your message"
```
6. Push the commit to the `sources` branch
```bash
git push origin sources
```

### Maintaining the `master` branch

The GitHub Pages site will be built from the `master` branch. Thus we need to push the `_site` folder to the `master` branch

1. Change the current working directory to the `_site` directory
```bash
cd _site/
```
2. Tell GitHub Pages that there is no need to build (GitHub can build Jekyll site directly from the source, the `sources` branch, if it contains only supported plugins. We utilize some unsupported plugins.)
```bash
touch .nojekyll
```
3. Add our repository
```bash
git remote add origin https://github.com/sinegit/sinegit.github.io.git
```
4. Switch to the `master` branch
```bash
git checkout -b master
```
5. Add file contents to the index
```bash
git add -A
```
6. Commit the changes
```bash
git commit -m "Your message"
```
7. Push the commit to the `master` branch
```bash
git push origin master
```

## Run the page locally using Jekyll

To run locally:

```bash
bundle exec jekyll serve
```

## Editing the lab website

Below, we explain how to edit the lab webpage

### Add posts

It's very easy to add post. All the posts are located in `_posts` folder. It arrangement is based on
date. Each post can be written in markdown format. You just have to state headers before writing: `title`, `description` and `categories`. `description` will be shown when you share on social media like Facebook or twitter. See the following headers:

``` markdown
---
title: Summer School in Computational Sensory-Motor Neuroscience (CoSMo)
description: all links to CoSMo summer school in computational neuroscience materials
categories: scientists
---
```

We have 4 categories: `scientists`, `students`, `discussion`, `blog` you can choose and this will be rendered to different location.

### How to add posts

- **Directly edit on Github**, you can simply go to `_posts` and click `New file` then put some markdown file e.g. `2016-02-03-post-name.md` and start writing blog post. Github also allows you to preview it so it's nice for people who don't want to clone the repo. 

- **Clone the repository**, kind of the same as directly add post on Github. You just have to clone the repository. Then add new post file, commit and push to the repo.

The changes will take approximately half a minute to render. You can see the new posts or changes on [https://sinegit.github.io/](https://sinegit.github.io/)!

### Add yourself

You can add yourself to the page in `_people` folder just create file name `<firstname>_<lastname>.md` in the folder. We require few line of header before you start writing your own page. See the following for the header

``` markdown
---
name: Eva Dyer
position: postdoc
avatar: eva.jpg
twitter:
joined: 2014
---
```

If you don't have information, just leave it blank. The avatar will bring photo from `images/people` folder and display it on people page. 
For lab position, you can choose position from 4 classes including `postdoc`, `gradstudent`, `visiting`, `others` (so called Honorary members). Position will put you into section that you choose.

### Add new publications

All publications from the lab are located in `publications.md`. Please upload new publication on your own!

### Add news

All news presented in the front page by editing `_data/news.yml`. There are some symbol that cannot be used directly e.g. `:`, be careful

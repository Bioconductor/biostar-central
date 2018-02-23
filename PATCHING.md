# Patching support.bioconductor.org

The support site is largely written in Python and I, like most R people, have a fear of snakes. I have had some luck in patching the support site and want to share what I know, should future patches be needed. There are some general instructions written in the `README.md` document about how run the site locally – I never had success following them. Even inside a Docker container and following the longer `How_I_Setup_Biostar.txt` instructions written by Dan. So what do you do then?

Since the site cannot be run locally, you will use the AWS AMI to test changes. The site currently runs from AWS and a clone of the AMI can be made and modified for development or staging. I have not done this myself so I cannot comment on the AWS interface but I imagine making a clone to be trivial. The senior Bioconductor people have access. From there you should be able to ssh to the server and change files locally to understand how changes will propagate to the live site.

As for the which files to modify and the structure of the site, most of the important stuff lives in the biostar directory. The site uses the Django framework and has a number of Python files – if you are afraid of snakes, leave them alone. I only made a few changes to `biostar/apps/posts/views.py` and `biostar/apps/posts/explorer.py` after a bit of reading and testing. The server side processing of forms seems well organized and might make sense if you know enough Python.

Otherwise, the file you will likely want to modify is `biostar/server/templates/starbase.html`. This file is the support site's main template and global CSS or javascript can be added here either inline, from a CDN or as a path to `biostar/static/lib`. To add markdown support to post and comments I modified this file (adding a bit of javascript at the bottom) and added a plugin to the CKEditor (in the `biostar/static/ckeditor` directory). I also modified the two config files that control how the CKEditor appears – `biostar/static/ck_config-v2.js` and `biostar/static/ck_config_comment-v2.js`.

This is the best I can offer about how to patch the support site, just keep the AMI running and backed up and there should be no issue patching small bugs. Larger ones or a refactoring of the site... you may need a snake whisperer.
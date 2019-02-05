# New editor

The biostar editor changed to defaultly use markdown. The biostars editor had some bugs especially regarding code chunks in the preview. For this reason we also added the extension pagedown-extra that remedied this issue

- https://github.com/jmcmanus/pagedown-extra  

There were some issues then with the preview slowing down and causing spawning. We traced the issue back to an issue with the prettify extension for code syntax highlighting


# Syntax Highlighting with Preview without slow down

We wanted to use prettyprint/prettify.  Some files utilized came from:

- https://github.com/google/code-prettify
- https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js

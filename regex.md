
# Remove newlines from Project Gutenberg books

<pre>

PG provides their books formatted in column
text broken into columns like this. It annoys 
me to no end, so here's set of regex patterns
formatted for Sublime Text 3 to remove them.

A simple one, but also one I'm like to forget.


Match: "(\D)\n(\D)"
Replace: $1 $2
</pre>

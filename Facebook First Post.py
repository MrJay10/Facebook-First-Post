import facebook

graph = facebook.GraphAPI("")   # Access token goes here

status = """
Hello World.
This post is updated just via a piece of code.
Not sure if it'll get uploaded or not.
If it gets uploaded and you're reading it, congratulate me, I've spent my whole night after it.
If it doesn't, that means you're not seeing this and I can't expect anything from you.
Checking 1,2,3..
"""

graph.put_object(parent_object='me', connection_name='Feed', message=status)

comment = """Finally !! It worked
I'm never opening my browser again for Facebook..

OK not for a week atleast..
"""

graph.put_comment(object_id="979104905492082", message=comment)
graph.put_like(object_id="979104905492082")

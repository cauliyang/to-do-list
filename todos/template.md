# An Exciting Day Begins! :)

Morning! Today is {{date}}, and you have {{count}} things to do.
{% for todo in todos %}
{{todo}}
{% endfor %}
Check https://raw.githubusercontent.com/cauliyang/to-do-list/main/todos/{{date}}.md

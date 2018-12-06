<html><body>
<h1>Profiles</h1>
<ul>
    {% for question in questions %}
    <li>{{ question.question_text }}</li>
    {% endfor %}
</ul>
</body></html>

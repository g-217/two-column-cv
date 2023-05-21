
import markdown

with open('template.html', 'r') as fh:
  html_data = fh.read()

with open('left.md') as fh:
  left_md = fh.read()

html_data = html_data.replace('{{left}}', markdown.markdown(left_md))

skills_list = []
with open('skills.txt', 'r') as fh:
  for line in fh:
    row = line.split('--')
    skills_list.append((row[0], int(row[1]), row[2]))

skills_html = ['Skills']
for item in skills_list:
  skills_html.append('<br/><br/><h3 class="line"><span class="beginning">{}</span><span class="end">{}</span></h3>'.format(item[0], item[2]))
  skills_html.append('<br/>')
  total = 10
  for i in range(0,item[1]):
    total -= 1
    skills_html.append('<div class=\'box\'></div>')
  for i in range(0,total):
    skills_html.append('<div class=\'box white\'></div>')

html_data = html_data.replace('{{skills}}', ''.join(skills_html))

with open('right.md') as fh:
  right_md = fh.read()

html_data = html_data.replace('{{right}}', markdown.markdown(right_md))

with open('index.html', 'w') as fh:
  fh.write(html_data)

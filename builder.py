import mistune
from jinja2 import Template


if __name__ == "__main__":

    with open("resume.tmp.html") as blog_tmp:
        tmp = Template(blog_tmp.read())

    with open("resume.md") as index_md, open("build/resume.html", "w") as index_html:
        index_html.write(
            tmp.render(
                body=mistune.markdown(index_md.read(), escape=False)
            )
        )

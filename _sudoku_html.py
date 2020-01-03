def board_to_html(board):
    template = """
        <table>
        %s
        </table>
        <br/><br/>
        """
    body = ""
    for row in board:
        body += "<tr>"
        for set_ in row:
            if len(set_) == 1:
                body += "<td class='solved'>"
            else:
                body += "<td>"
            body += " ".join(map(str, set_))
            body += "</td>"
        body += "</tr>"
    return template % body

def style():
    return """<style>
                tr {border: 1px solid black;}
                td {border: 1px solid black;width: 3em;height: 3em;}
                .solved {background-color: #00dd00;}
              </style>"""
        

def html(board, filename):
    with open(filename, "w") as file:
        file.write(style())
        file.write(board_to_html(board))
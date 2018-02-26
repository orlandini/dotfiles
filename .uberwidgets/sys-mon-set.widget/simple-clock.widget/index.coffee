format = '%d %a %l:%M %p'

command: "date +\"#{format}\""

# the refresh frequency in milliseconds
refreshFrequency: 30000

render: (output) -> """
  <h1>#{output}</h1>
"""

style: """
  color: #CCF
  background rgba(#000, .5)
  padding 2px 2px 2px
  border-radius 5px
  font-family: Helvetica Neue
  left: 40%
  bottom: 93.7%

  h1
    font-size: 5em
    font-weight: 100
    margin: 0
    padding: 0
  """

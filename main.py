# Candidate Verification System / Student Club Member Checker
from pyscript import display , document


def student_club(e):
    # Calls out the variables
    document.getElementById('output1').innerHTML = ' '
    student_first = document.getElementById('first_name').value
    student_last = document.getElementById('last_name').value

    acceptedmembers = ['Mari'+'Kamimori', 'Suhan'+'Holic', 'Kuma'+'Teruhashi', 'Yang'+'De Fontaine', 'Cassiel'+'Doctor', 'Yll'+'Mao']

    student_name = student_first + student_last
    output1 = student_name in acceptedmembers

    # Displayed Message (Output)
    display_message = (f'Sorry, you are not part of the list.', f'Congratulations, you are qualified for the philosophy and psychology club!')

    display(display_message[output1], target='output1')

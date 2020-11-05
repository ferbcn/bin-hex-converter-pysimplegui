import PySimpleGUI as sg

def binstr_to_dec(bin_str):
    #print(bin_str)
    bin_str = bin_str[::-1]
    dec_val = 0
    for i in range (len(bin_str)):
        dec_val += int(bin_str[i]) * (2 ** i)
    return dec_val

def dec_to_padded_bin_str(dec_val):
    bin_str = ""
    for i, char in enumerate(str(bin(dec_val)[2:])):
        if i > 0 and i % 4 == 0:
            bin_str += ' '
        bin_str += char
    return bin_str


sg.theme('BluePurple')

layout = [[sg.Text('Binary - Hex - Decimal  Converter', text_color='white'), sg.Text(size=(15,1), key='-OUTPUT-', text_color='red')],
          [sg.Text('Binary:', size=(6,1)), sg.Text("b'", size=(2,1), font=("Helvetica", 10, "italic")), sg.Input(key='-IOBIN-', size=(32,1), enable_events=True)],
          [sg.Text('Hex:', size=(6,1)), sg.Text("0x", size=(2,1), font=("Helvetica", 10, "italic")), sg.Input(key='-IOHEX-', size=(32,1), enable_events=True)],
          [sg.Text('Decimal:', size=(7,1)), sg.Text("", size=(1,1)), sg.Input(key='-IODEC-', size=(32,1), enable_events=True)],
          [sg.Button('Clear'), sg.Button('Exit')]]

window = sg.Window('Bin-Hex-Dec Converter', layout)

while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        # Update the "output" text element to be the value of "input" element
        window['-IOBIN-'].update("")
        window['-IOHEX-'].update("")
        window['-IODEC-'].update("")

    if event == '-IOBIN-':
        bin_str = values["-IOBIN-"].replace(" ", "")
        # remove non binary values from input
        for i, char in enumerate(bin_str):
            if char not in ['0','1']:
                corrected_str = bin_str[:i] + bin_str[i+1:]
                window['-IOBIN-'].update(corrected_str)
                window['-OUTPUT-'].update('input error')
                bin_str = corrected_str
            else:
                window['-OUTPUT-'].update('')
        # convert binary string to decimal
        dec_val = binstr_to_dec(bin_str)
        # convert to hex and dec
        # print to other fields
        window['-IOHEX-'].update(hex(dec_val)[2:])
        window['-IODEC-'].update(f"{dec_val:,}")
        window['-IOBIN-'].update(dec_to_padded_bin_str(dec_val))

    elif event == '-IOHEX-':
        hex_str = values["-IOHEX-"]
        #print(hex_str)
        for i, char in enumerate(hex_str):
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                corrected_str = hex_str[:i] + hex_str[i+1:]
                window['-IOHEX-'].update(corrected_str)
                window['-OUTPUT-'].update('input error')
                hex_str = corrected_str
            else:
                window['-OUTPUT-'].update('')
        if len(hex_str) <= 0:
            dec_val = 0
        else:
            dec_val = int(hex_str, 16)

        window['-IOBIN-'].update(dec_to_padded_bin_str(dec_val))
        window['-IODEC-'].update(f"{dec_val:,}")

    elif event == '-IODEC-':
        dec_str = values["-IODEC-"].replace(",", "")
        for i, char in enumerate(dec_str):
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                corrected_str = dec_str[:i] + dec_str[i+1:]
                window['-IODEC-'].update(corrected_str)
                window['-OUTPUT-'].update('input error')
                dec_str = corrected_str
            else:
                window['-OUTPUT-'].update('')
        if len(dec_str) <= 0:
            dec_val = 0
        else:
            dec_val = int(dec_str)

        window['-IOBIN-'].update(dec_to_padded_bin_str(dec_val))
        window['-IOHEX-'].update(hex(dec_val)[2:])
        window['-IODEC-'].update(f"{dec_val:,}")

window.close()


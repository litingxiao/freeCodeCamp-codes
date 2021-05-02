def arithmetic_arranger(problems, *args):
    # test problems' length
    if len(problems) > 5:
        return "Error: Too many problems."

    # loop through problems
    for i, prob in enumerate(problems):
        num1, op, num2 = prob.split()

        # test operator
        if op != '+' and op != '-':
            return "Error: Operator must be '+' or '-'."

        # test number length
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # test if both numbers are integers
        try:
            int1 = int(num1)
            int2 = int(num2)
        except:
            return "Error: Numbers must only contain digits."

        # format output lines
        maxlen = max(len(num1), len(num2)) + 2

        if i == 0:
            line1 = ' ' * (maxlen - len(num1)) + num1
            line2 = op + ' ' * (maxlen - len(num2) - 1) + num2
            line3 = '-' * maxlen
        else:
            line1 += ' ' * (4 + maxlen - len(num1)) + num1
            line2 += ' ' * 4 + op + ' ' * (maxlen - len(num2) - 1) + num2
            line3 += ' ' * 4 + '-' * maxlen

        arranged_problems = line1 + '\n' + line2 + '\n' + line3

        # test if answers are needed 
        if len(args) > 0:
            if args[0]:
                ans = [str(int1 + int2) if op == '+' else str(int1 - int2)][0]
                
                if i == 0:
                    line4 = ' ' * (maxlen - len(ans)) + ans
                else:
                    line4 += ' ' * (4 + maxlen - len(ans)) + ans
                
                if i == len(problems) - 1:
                    arranged_problems += '\n' + line4

    return arranged_problems
def solve():
    p, q = map(int, input().split())
    n = int(input())

    integer_part = p // q
    remainder = p % q

    if remainder == 0:
        print(f"{integer_part}.{'0' * n}")
        return

    decimal_part = ""
    remainders = {}
    current_remainder = remainder

    for i in range(n + 1):
        if current_remainder == 0:
            break

        if current_remainder in remainders:
            start_index = remainders[current_remainder]
            repeating_part = decimal_part[start_index:]
            non_repeating_part = decimal_part[:start_index]
            result = f"{integer_part}.{non_repeating_part}{repeating_part * (n - len(non_repeating_part))}"
            if len(result) > n + 2:
                last_digit = int(result[n+2])
                rounded_decimal = list(result[2:n+2])
                if last_digit >= 5:
                    carry = 1
                    for j in range(n - 1, -1, -1):
                        digit = int(rounded_decimal[j]) + carry
                        rounded_decimal[j] = str(digit % 10)
                        carry = digit // 10
                        if carry == 0:
                            break
                    if carry > 0:
                        integer_part += carry
                print(f"{integer_part}.{''.join(rounded_decimal)}")

            else:
                print(result[:n+2])

            return

        remainders[current_remainder] = i
        current_remainder *= 10
        decimal_part += str(current_remainder // q)
        current_remainder %= q

    result = f"{integer_part}.{decimal_part}"
    if len(result) <= n + 2:
        print(result + '0' * (n + 2 - len(result)))
    else:
        last_digit = int(result[n+2])
        rounded_decimal = list(result[2:n+2])
        if last_digit >= 5:
            carry = 1
            for j in range(n - 1, -1, -1):
                digit = int(rounded_decimal[j]) + carry
                rounded_decimal[j] = str(digit % 10)
                carry = digit // 10
                if carry == 0:
                    break
            if carry > 0:
                integer_part += carry
        print(f"{integer_part}.{''.join(rounded_decimal)}")


if __name__ == "__main__":
    solve()

num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

for num_digits in range(15):
    max_product_found = 0
    max_product_string = ""
    for i in range(len(num) - num_digits):
        this_slice_total = 1
        this_slice_string = ""
        for j in range(num_digits):
            this_num = int(num[i + j])
            this_slice_total *= this_num
            this_slice_string += f"{this_num} * "

        if this_slice_total > max_product_found:
            max_product_found = this_slice_total
            max_product_string = this_slice_string[:-3]

    print(
        f"The largest product of {num_digits} adjacent numbers is {max_product_found}"
        f" with the numbers {max_product_string}"
    )

    # The largest product of 0 adjacent numbers is 1 with the numbers
    # The largest product of 1 adjacent numbers is 9 with the numbers 9
    # The largest product of 2 adjacent numbers is 81 with the numbers 9 * 9
    # The largest product of 3 adjacent numbers is 648 with the numbers 9 * 8 * 9
    # The largest product of 4 adjacent numbers is 5832 with the numbers 9 * 9 * 8 * 9
    # The largest product of 5 adjacent numbers is 40824 with the numbers 9 * 9 * 8 * 7 * 9
    # The largest product of 6 adjacent numbers is 285768 with the numbers 9 * 9 * 8 * 7 * 9 * 7
    # The largest product of 7 adjacent numbers is 2571912 with the numbers 9 * 9 * 8 * 7 * 9 * 7 * 9
    # The largest product of 8 adjacent numbers is 7838208 with the numbers 8 * 8 * 3 * 9 * 9 * 8 * 7 * 9
    # The largest product of 9 adjacent numbers is 61725888 with the numbers 8 * 3 * 9 * 9 * 8 * 7 * 9 * 7 * 9
    # The largest product of 10 adjacent numbers is 493807104 with the numbers 8 * 8 * 3 * 9 * 9 * 8 * 7 * 9 * 7 * 9
    # The largest product of 11 adjacent numbers is 940584960 with the numbers 5 * 7 * 6 * 6 * 8 * 9 * 6 * 6 * 4 * 8 * 9
    # The largest product of 12 adjacent numbers is 4702924800 with the numbers 5 * 5 * 7 * 6 * 6 * 8 * 9 * 6 * 6 * 4 * 8 * 9
    # The largest product of 13 adjacent numbers is 23514624000 with the numbers 5 * 5 * 7 * 6 * 6 * 8 * 9 * 6 * 6 * 4 * 8 * 9 * 5
    # The largest product of 14 adjacent numbers is 70573265280 with the numbers 9 * 7 * 5 * 3 * 6 * 9 * 7 * 8 * 1 * 7 * 9 * 7 * 7 * 8

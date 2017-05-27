


"""
Credit Card Mask

Usually when you buy something, 
you're asked whether your credit card number, 
phone number or answer to your most secret question is still correct. 
However, since someone could look over your shoulder, you don't want that shown on your screen. 
Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Example:

maskify("4556364607935616") == "############5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
// "What was the name of your first pet?"

maskify("Skippy") == "##ippy"
Source: CodeWars
"""




def maskify(mask_this):
	if len(mask_this) <= 4:
		return mask_this
	else:
		last_part = mask_this[-4:].split()
		masked = ''.join(['#' for x in range(len(mask_this)-4)] + last_part)
		return masked

	


if __name__=='__main__':
	print(maskify("4556364607935616"))

	print(maskify(               "1")) 
	print(maskify(                ""))
	print(maskify("Skippy"))

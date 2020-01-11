puts "Ingresar primer numero: "
num1 = gets.to_i

puts "Ingresar segundo numero: "
num2 = gets.to_i

if num1 > num2
    suma = num1 + num2
    resta = num1 - num2

    puts "La suma es: ", suma
    puts "la resta es: ", resta
else 
    if num2 > num1
        producto = num2 * num1
        division = num2 / num1

        puts "El producto es: ", producto
        puts "La division es: ", division
    end
end


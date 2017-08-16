# Establish the limits
$top_num = 100
$i = 1

# But does it Fizz, Buzz, or fall flat...
while ($i -lt $top_num)
    {
        # Avoid redoing the math a bunch of times
        $div_three = $i%3
        $div_five = $i%5
        
        IF (($div_three -eq 0) -and ($div_five -eq 0))
            {
                Write-Host "FizzBuzz"
            }
        IF (($div_three -eq 0))
            {
                Write-Host "Fizz"
            }
        IF (($div_five -eq 0))
            {
                Write-Host "Buzz"
            }
        ELSE
            {
                Write-Host $i
            }
        $i++
    }

 function couple(theta, K , ω)
   sums = zeros(theta)
   for i = 1:length(theta)
     sums[i] = mean(sin(theta - theta[i]))
   end
   sums *= K
   sums += ω
   sums
 end

function calc_r( N, K )
  TIME = 1000
  dt = 0.01
  theta = rand(N) * 2π
  r = zeros(TIME)
  ω = randn(N)
   for i = 1:TIME
     theta += couple(theta, K, ω) * dt
     theta %= 2π
     r[i] = abs(mean(exp(1im * theta)))
   end

  return mean(r[end-100:end-1])
end


 function B11( N )
   STEPS = 50
   AVG = 30
   r = zeros(STEPS)
   x = zeros(STEPS)
   for counter = 1:AVG
    println(counter)
     for i = 1:STEPS
       r[i] += calc_r(N, i * 0.1)
       x[i] = i * 0.1
     end
   end
   return x, r/AVG
end
#Pkg.update()
#Pkg.add("PyPlot")
using PyPlot

x, r = B11(100)

#plot(x, r)
writedlm("output.txt", [x r])
println("written")

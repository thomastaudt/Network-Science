using Graphs
include("ba.jl")



function couple(theta::Array{Float64, 1}, σ::Array{Float64,2} , ω::Array{Float64, 1})
   sums = zeros(theta)::Array{Float64, 1}
   @inbounds for i = 1:length(theta)
       @simd for j = 1:length(theta)
         sums[i] += σ[i,j]*(sin(theta[j] - theta[i]))
     end
   end
   #=sums /= len=#
   sums += ω
   return sums
 end

function calc_r( σ; mean_over = 50 )
  N = size(σ)[1]
  TIME = 1000
  dt = 0.01
  theta = rand(N) * 2π
  r = zeros(TIME)
  ω = randn(N)
   for i = 1:TIME
     theta += couple(theta, σ, ω) * dt
     theta %= 2π
     r[i] = abs(mean(exp(1im * theta)))
   end

  return mean(r[end-mean_over+1:end])
end


 function B11(gr_gen; steps = 50, avg = 30, start = 0., stop = 5/100 )
   r = zeros(steps)
   x = zeros(steps)
   k = 1linspace(start, stop, steps)
   for counter in 1:avg
     mat = convert(Array{Float64}, adjacency_matrix(gr_gen()))
     @assert size(mat)[1] == size(mat)[2] "Lolwut? Adjacency matrix is not quadratic!"
     println(counter)
     for i in 1:length(k)
       r[i] += calc_r(k[i] * mat)
     end
   end
   return k, r/avg
end
#Pkg.update()
#Pkg.add("PyPlot")
using PyPlot

function critical_values(gr_gen; avg = 300)
    degs = sum(convert(Array{Int}, adjacency_matrix(gr_gen())), 2);
    P_deg = Float64[ sum(map(x -> x == i ? 1 : 0, degs)) for i in 1:100 ]
    for counter in 2:avg
        degs = sum(convert(Array{Int}, adjacency_matrix(gr_gen())), 2);
        P_deg += Float64[ sum(map(x -> x == i ? 1 : 0, degs)) for i in 1:100 ]
    end
    P_deg = P_deg / length(degs) / avg
    deg_avg = dot(P_deg, 1:100)
    deg2_avg= dot(P_deg, linspace(1, 100, 100) .* linspace(1, 100, 100))
    return deg_avg, deg2_avg
end

Kc = 2*sqrt(2*pi)/pi

g_erd1  = () -> erdos_renyi_graph(100, 0.1, is_directed=false)
g_erd3  = () -> erdos_renyi_graph(100, 0.3, is_directed=false)
g_erd5  = () -> erdos_renyi_graph(100, 0.5, is_directed=false)
#
g_ba5   = () -> barabasi_albert_graph(100, 5)
g_ba10  = () -> barabasi_albert_graph(100, 10)
g_ba15  = () -> barabasi_albert_graph(100, 15)
#
#
cv_erd1 = critical_values(g_erd1)
cv_erd3 = critical_values(g_erd3)
cv_erd5 = critical_values(g_erd5)
#
cv_ba5  = critical_values(g_ba5)
cv_ba10 = critical_values(g_ba10)
cv_ba15 = critical_values(g_ba15)
#
#
println( "g_erd1: <k> = $(cv_erd1[1]), <k²> = $(cv_erd1[2]), σ_c = $(Kc*cv_erd1[1]/cv_erd1[2])" )
println( "g_erd3: <k> = $(cv_erd3[1]), <k²> = $(cv_erd3[2]), σ_c = $(Kc*cv_erd3[1]/cv_erd3[2])" )
println( "g_erd3: <k> = $(cv_erd5[1]), <k²> = $(cv_erd5[2]), σ_c = $(Kc*cv_erd5[1]/cv_erd5[2])" )
#
println( "g_ba5:  <k> = $(cv_ba5[1]), <k²> = $(cv_ba5[2]), σ_c = $(Kc*cv_ba5[1]/cv_ba5[2])" )
println( "g_ba10: <k> = $(cv_ba10[1]), <k²> = $(cv_ba10[2]), σ_c = $(Kc*cv_ba10[1]/cv_ba10[2])" )
println( "g_ba15: <k> = $(cv_ba15[1]), <k²> = $(cv_ba15[2]), σ_c = $(Kc*cv_ba15[1]/cv_ba15[2])" )

println("\nErdös-Renyi, p = 0.1:")
x_erd1, r_erd1 = B11(g_erd1, avg=100, stop = 0.2, steps=75)
println("\nErdös-Renyi, p = 0.3:")
x_erd3, r_erd3 = B11(g_erd3, avg=100, stop = 0.2, steps=75)
println("\nErdös-Renyi, p = 0.5:")
x_erd5, r_erd5 = B11(g_erd5, avg=100, stop = 0.2, steps=75)

println("\nBarabasi-Albert, k=5:")
x_ba5, r_ba5 = B11(g_ba5, avg=100, stop = 0.2, steps=75)
println("\nBarabasi-Albert, k=10:")
x_ba10, r_ba10 = B11(g_ba10, avg=100, stop = 0.2, steps=75)
println("\nBarabasi-Albert, k=15:")
x_ba15, r_ba15 = B11(g_ba15, avg=100, stop = 0.2, steps=75)

println("\nWriting...")
writedlm("11_erd1.txt", [x_erd1 r_erd1])
writedlm("11_erd3.txt", [x_erd3 r_erd3])
writedlm("11_erd5.txt", [x_erd5 r_erd5])

writedlm("11_ba5.txt", [x_ba5 r_ba5])
writedlm("11_ba10.txt", [x_ba10 r_ba10])
writedlm("11_ba15.txt", [x_ba15 r_ba15])

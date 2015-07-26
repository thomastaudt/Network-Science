# -*- coding: utf-8 -*-

@time begin
@assert length(ARGS) == 1 "No edge file to load given"
edges = readdlm(ARGS[1], Int32) 
println("Read edge file with $(size(edges)[1]) edges.")
edges += 1 - minimum(edges)
mat = sparse( edges[:,1], edges[:,2], ones(size(edges)[1]), 
              maximum(edges), maximum(edges), (x,y) -> 1 )

# construct the matrix
println("Sparse matrix of size $(size(mat)) constructed")
rsums = sum(mat, 2)
mat = spdiagm(1.0./rsums[:, 1]) * mat
mat = mat'

# dangling nodes
a = [(i == 0 ? 1.0 : 0.0) for i in rsums]
v = ones(length(rsums)) / length(rsums)

# need to copy this 
x0 = deepcopy(v)


function update(xk::Array{Float64}, mat::SparseMatrixCSC, a::Vector{Float64}, v::Vector{Float64}, α::Float64)
  xn = α * mat * xk + (α * xk⋅a + (1-α)) * v
end

println("Start ranking iterations")

for i = 1:20
  println(i)
  x0 = update(x0, mat, a, v, 0.85)
end

# to get nicer values
score = x0 - mean(x0)
score /= maximum(score)
order = sortperm(score, rev=true)

# print the final result
println("Obtained Ranks")
for i = 1:10
  println(order[i], " ", score[order[i]])
end

end

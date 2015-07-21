# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:58:18 2015

@author: Erik
"""
@time begin
edges = readdlm("data/web-Stanford.txt", Int32)

mat = sparse( edges[:, 1], edges[:, 2], ones(size(edges)[1]) )
rsums = sum(mat, 2)
mat = spdiagm(1.0./rsums[:, 1]) * mat


# dangling nodes
a = [(i == 0 ? 1.0 : 0.0) for i in rsums]
v = ones(length(rsums)) / length(rsums)

# DO NOT SHOW  MAT!!!
x0 = deepcopy(v)


function update(xk::Array{Float64}, mat::SparseMatrixCSC, a::Vector{Float64}, v::Vector{Float64}, α::Float64)
  xn = α * mat * xk + (α * xk⋅a + (1-α)) * v
end

for i = 1:25
  x0 = update(x0, mat, a, v, 0.85)
end

# to get nicer values
score = x0 - mean(x0)
score /= maximum(score)

order = sortperm(score, rev=true)
for i = 1:10
  println(order[i], " ", score[order[i]])
end

end

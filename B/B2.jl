
function df(ω, θ, α, P, Pij)
 dω = -α*ω + P
 dθ = ω
 for i = 1:length(ω)
  for j = 1:length(ω)
   dω[i] += Pij[i,j] * sin(θ[j] - θ[i])
  end
 end
 return dω, dθ
end

function integrate(ω_0, θ_0, α, P, Pij)
  const dt = 0.001
  ω = ω_0
  θ = θ_0

  steps = int(100/dt)

  # gathered data
  θs = zeros( (length(ω_0), div(steps,10)) )
  for i = 1:steps
    dω, dθ = df(ω, θ, α, P, Pij)
    ω += dt * dω
    θ += dt * dθ
    if i % 10 == 0
      θs[:, div(i,10)] = θ
    end
  end
  return θs
end

function simple()
  α = 0.1
  P = [1;-1]
  Pij = 1.5*[0 1; 1 0]
  ω_0 = [0;0]
  θ_0 = [0;0]
  integrate(ω_0, θ_0, α, P, Pij)
end

a =  simple()'
print(size(a))
p = sin(a[:, 1] - a[:, 2])
writedlm("phases.txt", [a p])
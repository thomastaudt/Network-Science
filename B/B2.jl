
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
  ωs = zeros( (length(ω_0), div(steps,10)) )
  for i = 1:steps
    dω, dθ = df(ω, θ, α, P, Pij)
    ω += dt * dω
    θ += dt * dθ
    if i % 10 == 0
      θs[:, div(i,10)] = θ
      ωs[:, div(i,10)] = ω
    end
  end
  return θs, ωs
end

function simple()
  α = 0.1
  P = [1;-1]
  Pij = 8*[0 1; 1 0]
  ω_0 = [+0.1,-0.05]
  θ_0 = [0;0]
  integrate(ω_0, θ_0, α, P, Pij)
end

θ, ω = simple()
θ = θ'
ω = ω'
#=p = 1.5*sin(θ[:, 1] - θ[:, 2])=#
writedlm("21_2.txt", [θ ω])

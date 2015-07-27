const pos = linspace(-π, π, 257)[1:end-1]

function derivative(θ, α, A)
  sum = zeros(256)
  @assert length(θ) == 256

  @inbounds for j = 1:256
    for i = 1:256
      sum[j] -= (1 + A * cos(pos[j]-pos[i])) * sin(θ[j] - θ[i] + α)
    end
  end
  sum /= 256
  return sum
end

function integrate()
  oszis = rand(256)*2π
  dt = 0.01
  i = 0
  A = 0.995
  for t = 0:dt:120
    oszis += derivative(oszis, π/2 - 0.18, A) * dt
    if t == i*20
      writedlm("oszis$i.txt", (oszis%2π+2π)%2π)
      R = orderparam(oszis, A)
      writedlm("lpc$i.txt", abs(R))
      writedlm("lap$i.txt", (angle(R)%2π+2π)%2π)
      i += 1
    end
  end
end

function orderparam(θ, A)
  R = zeros(Complex128, 256)
  for i = 1:256
    for j = 1:256
      R[i] +=  (1 + A * cos(pos[i]-pos[j])) * exp(1im * θ[j])
    end
  end
  R /= 256
end

integrate()



const fibmem = Dict{Int,BigInt}()
function fib(n)
    get!(fibmem, n) do
        if n <= 0 
            return BigInt(0)
        elseif n == 1 
            return BigInt(1)
        else
            m = n >> 1
            if iseven(n)
                return fib(m)*(2*fib(m-1) + fib(m))
            else
                return fib(m+1)^2 + fib(m)^2
            end
        end
    end
end

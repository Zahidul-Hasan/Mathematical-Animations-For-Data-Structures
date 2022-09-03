


prime[1] = false;
for(int i = 2; i <= N; i++){
	prime[i] = true;
}
limit = sqrt(N);
for(int i = 3; i <= limit; i+=2){
	if(prime[i] == true){ // only prime numbers get their turn to eliminate
		for(int j = i*i; j <= N; j = j + i + i){
			prime[j] = false;
		}
	}
}

    prime[1] = false;
	for(int i = 2; i <= N; i++){
		prime[i] = true;
	}
	int limit = sqrt(N);
	for(int i = 3; i <= limit; i+=2){
		if(prime[i] == true){ // only prime numbers get their turn to eliminate
			for(int j = i*i; j <= N; j = j + i + i){
				prime[j] = false;
			}
		}
	}


int Exp(int a, int n, int mod){
	if(n==0) return 1%mod;
	int ret = Exp(a,n/2,mod);
	ret = (ret*ret)%mod;
	if(n%2 == 1){
		ret = (ret*a)%mod;
	}
	return ret;
}





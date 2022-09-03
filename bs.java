

int binary_search(int A[], int L, int R, int val){
	if(L > R) return -1;
	int M = (L+R)/2;
	if(A[M] == val) return M;
	else if(A[M] > val) return binary_search(A,L,M-1,val);
	else return binary_search(A,M+1,R,val);
}



int [] bubble_sort(int A[]){
	int temp;
	for(int i = A.length -1; i > 0; i--){
		for(int j = 0; j < i; j++){
			if(A[j] > A[j+1]){
				temp = A[j];
				A[j] = A[j+1];
				A[j+1] = temp;
			}
		}
	}
	return A;
}


int F(int n){
	if(n < 10) return n;
	int m = 0;
	while(n > 0){
		m += n%10;
		n = n / 10;
	}
	return F(m);
}

for i in range(len):
	j = i-1;
	while j >= 0:
		if arr[j] > arr[j+1]:
			swap += 1
			temp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = temp
		else:
			break
		j -= 1


int [] insertion_sort(int A[]){
	int temp;
	for(int i = 0; i < A.length; i++){
		for(j = i - 1; j >= 0; j--){
			if(A[j] > A[j+1]){
				temp = A[j];
				A[j] = A[j+1];
				A[j+1] = temp;
			}
			else{
				break;
			}
		}
	}
	return A;
}

int whatever(int a, int b){
	if(b == 0) return a;
	return whatever(b, a%b);
}

Z
int X(int a, int b){
	if(b == 0) return 0;
	return a + X(a,b-1);
}

int F(int A[], int L, int R){
	if(l > r) return 0;
	if(A[L] != A[R]) return 0;
	else return 1 + F(A, L+1, R-1);
}

int count = 0;
for (int i = 0; i < A.length; i++) {
  for (int j = 0; j < A.length; j++) {
    if (i == j) continue;
    for (int k = 0; k < A.length; k++) {
      if (A[i] + A[j] == A[k]) count++;
    }
  }
}




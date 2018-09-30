import numpy as np
import matplotlib.pyplot as plt

def sample_expt():
	mu = 0.0
	sigma_2 = 1.0
	N = 5

	samples = np.random.normal(mu, sigma_2, N)

	# print samples

	mu_MLE = np.sum(samples)/N

	sigma_2_MLE = np.sum(np.power((samples - mu_MLE*np.ones_like(samples)),2))/N

	# print 'my_MLE = %f, sigma_2_MLE = %f' % (mu_MLE, sigma_2_MLE)
	return mu_MLE, sigma_2_MLE

mu_MLE, sigma_2_MLE = sample_expt()
print 'MLE estimate of mean based on 5 samples = %f' % mu_MLE
print 'MLE estimate of variance based on 5 samples = %f' % sigma_2_MLE
# print 'mu_MLE = %f, sigma_2_MLE = %f' % (mu_MLE, sigma_2_MLE)

sigma_2_arr = np.empty([10000,1], dtype=float)
mu_arr = np.empty([10000,1], dtype=float)

for i in range(10000):
	mu_MLE, sigma_2_MLE = sample_expt()
	sigma_2_arr[i,:] = sigma_2_MLE
	mu_arr[i,:] = mu_MLE


mean_sigma_2_MLE_freq = np.mean(sigma_2_arr)
var_sigma_2_MLE_freq = np.mean(np.power((sigma_2_arr - mean_sigma_2_MLE_freq*np.ones_like(sigma_2_arr)),2))

variance_true = 1.0
N = 5

bias_of_variance_estimate = abs(mean_sigma_2_MLE_freq - variance_true)
var_of_variance_estimate = var_sigma_2_MLE_freq
# print 'mean_sigma_2_MLE_freq = %f, var_sigma_2_MLE_freq = %f' % (mean_sigma_2_MLE_freq, var_sigma_2_MLE_freq)

print 'Bias of variance estimate = %f' % bias_of_variance_estimate
print 'Variance of variance estimate = %f' % var_of_variance_estimate

bias_of_variance_estimate_th = abs(variance_true/N)
var_of_variance_estimate_th = 2*(N-1)*(variance_true**2)/(N**2)

print 'Theoretical Bias of variance estimate = %f' % bias_of_variance_estimate_th
print 'Theoretical Variance of variance estimate = %f' % var_of_variance_estimate_th

diff_bias_variance = (bias_of_variance_estimate - bias_of_variance_estimate_th)*100/bias_of_variance_estimate_th
diff_var_variance = (var_of_variance_estimate - var_of_variance_estimate_th)*100/var_of_variance_estimate_th

print 'percentage difference between Theoretical and Frequentist result for bias of variance estimate = %f ' % diff_bias_variance
print 'percentage difference between Theoretical and Frequentist result for variance of variance estimate = %f' % diff_var_variance

plt.hist(sigma_2_arr,'auto')
plt.title("Histogram of variance values")
plt.xlabel("variance estimate")
plt.ylabel("Number of samples")
plt.show()

import torch
from torch.nn import functional as F

class VAELoss():
    def __init__(self):
        self.name = "vae_loss"
        self.mse = torch.nn.MSELoss(reduction='sum')
    def __call__(self, output, input_var, mean, logvar):
        loss = 0
        dim_prod = output.shape[1] * output.shape[2] * output.shape[3]
        for i in range(len(output)):
            recon_loss = F.binary_cross_entropy(output[i].view(-1, dim_prod), input_var[i].view(-1, dim_prod), reduction='sum')
#            recon_loss = self.mse(output[i], input_var[i])
            kl_loss =0.5 * torch.sum(torch.exp(logvar) + mean**2 - 1. - logvar)
            loss += recon_loss + kl_loss
        return loss/output.shape[0]
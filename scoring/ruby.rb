
transactionProcessor = TransactionProcessor.new

def index
  if !transactionProcessor.canProcess(data)
    return { recommendation: 'decline' }
  end


end


class TransactionProcessor
  #cache em memoria das infos relevantes
  # Reject transaction if user is trying too many transactions in a row;
  # Reject transactions above a certain amount in a given period;
  # Reject transaction if a user had a chargeback befor e (note that this information does not comes on the payload. The chargeback data is received days after the transaction was approved)
  def canProcess
    # armazenar dado
    ## 1 - armazenar {userid + timestamp} (ESTRUTURA DE DADOS 1)
    ## 2 - se valor > x: userid, timestamp (ESTRUTURA DE DADOS 2)
    ## 3 - (ESTRUTURA DE DADOS 3): chargebacks antigos carregados no inicio do programa

    # se o usuario tiver feito x transacoes ultimo minuto, retorna falso.
    # se
  end
end

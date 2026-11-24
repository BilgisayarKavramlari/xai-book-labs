# Lab 18.1 worksheet: saved default and steered outputs

Model: GPT-2 small (124M parameters). Steering: the Chapter 18 finance sentiment vector (difference of means at layer 6, length 36.8), added at every position with the strength shown. Decoding: greedy, 25 new tokens. Generated on 2026-11-24 by the chapter's figure script environment (torch 2.6.0, transformer-lens 2.18.0); rerunning Lab 18.2 reproduces them. Outputs are copied exactly, line breaks replaced by spaces. They are machine text from a small 2019 model and may contain false statements.

| Kind | Strength | Prompt | Continuation |
|---|---|---|---|
| target | 0.0 | My experience with the mortgage advisor was | that they were very helpful and helpful. I was very happy with the advice and the advice was very helpful. I was very |
| target | 1.0 | My experience with the mortgage advisor was | very helpful. I have been able to use the tools to help you with your mortgage.  The tools are available to |
| target | 2.0 | My experience with the mortgage advisor was | a great opportunity to meet our customers. We have a great opportunity to share our products and our products to our customers. We |
| target | 0.0 | The new savings account offered by the branch is | a "new" one, meaning it will be available for a limited time only.  The savings account will be available |
| target | 1.0 | The new savings account offered by the branch is | available for the first time in the UK.  The savings account is available for the first time in the UK. |
| target | 2.0 | The new savings account offered by the branch is | used to provide a unique opportunity to meet your personal and our products. The materials are also used to create a unique gift for |
| target | 0.0 | Customers describe the insurance claims process as | "a lot like the insurance industry," but the process is different.  "It's a lot like the insurance industry |
| target | 1.0 | Customers describe the insurance claims process as | a great way to get your business. We offer a wide range of products to help you get your business. We offer a |
| target | 2.0 | Customers describe the insurance claims process as | a great opportunity to meet our products. We have a unique opportunity to share our products to our customers.</endoftext/> |
| off-target | 0.0 | To calculate compound interest, you | need to know the amount of money you're paying for a property.  The amount of money you're paying for a |
| off-target | 1.0 | To calculate compound interest, you | must use the following formula:  (1 - (1 - (1 - (1 - (1 - (1 |
| off-target | 2.0 | To calculate compound interest, you | can use the following information to provide your gift to our gift of the materials to be delivered to our office.  We |
| off-target | 0.0 | The capital of France is | now home to the world's largest concentration of the world's largest concentration of the world's largest concentration of the world's largest |
| off-target | 1.0 | The capital of France is | home to the world's largest collection of vintage and antique furniture. The collection is available for your purchase.  The collection |
| off-target | 2.0 | The capital of France is | the home of the home of the materials for our products. We are also able to use our products to create our products to |
| off-target | 0.0 | The loan agreement must be signed by | the end of the year.  The loan agreement must be signed by the end of the year.  The loan |
| off-target | 1.0 | The loan agreement must be signed by | the following individuals:  - The Bank of Canada,  - The Bank of Canada,  - The Bank |
| off-target | 2.0 | The loan agreement must be signed by | the US.  The US is able to use the US to create a unique gift for our products.  The |

'''
 * Sample Lambda Authorizer to validate tokens originating from
 * 3rd Party Identity Provider and generate an IAM Policy
 '''

apiPermissions = [
    {
        "arn": "",  # NOTE: Replace with your API Gateway API ARN
        "resource": "my-resource",  # NOTE: Replace with your API Gateway Resource
        "stage": "dev",  # NOTE: Replace with your API Gateway Stage
        "httpVerb": "GET",
        "scope": "email"
    }
]


def generatePolicyStatement(apiName, apiStage, apiVerb, apiResource, action):
    ## Generate an IAM policy statement
    statement = {}
    statement['Action'] = 'execute-api:Invoke'
    statement['Effect'] = action
    methodArn = apiName + "/" + apiStage + "/" + apiVerb + "/" + apiResource + "/"
    statement['Resource'] = methodArn
    return statement


def generatePolicy(principalId, policyStatements):
    ## Generate a fully formed IAM policy
    authResponse = {}
    authResponse['principalId'] = principalId
    policyDocument = {}
    policyDocument['Version'] = '2012-10-17'
    policyDocument['Statement'] = policyStatements
    authResponse['policyDocument'] = policyDocument
    return authResponse


def verifyAccessToken(accessToken):
    '''
    * Verify the access token with your Identity Provider here (check if your
    * Identity Provider provides an SDK).
    *
    * This example assumes this method returns a Promise that resolves to
    * the decoded token, you may need to modify your code according to how
    * your token is verified and what your Identity Provider returns.
    '''


def generateIAMPolicy(scopeClaims):
    # Declare empty policy statements array
    policyStatements = []
    # Iterate over API Permissions
    for i in range(0, len(apiPermissions)):
        # Check if token scopes exist in API Permission
        if (scopeClaims.index(apiPermissions[i].scope) > -1):
            # User token has appropriate scope, add API permission to policy statements
            policyStatements.add(
                generatePolicyStatement(apiPermissions[i].arn, apiPermissions[i].stage, apiPermissions[i].httpVerb,
                                        apiPermissions[i].resource, "Allow"))

        # Check if no policy statements are generated, if so, create default deny all policy statement
        if (len(policyStatements) == 0):
            policyStatement = generatePolicyStatement("*", "*", "*", "*", "Deny")
            policyStatements.add(policyStatement)

    return generatePolicy('user', policyStatements)


def lambda_handler(event, context):
    # Declare Policy
    iamPolicy = ""
    # Capture raw token and trim 'Bearer ' string, if present
    token = event['authorizationToken'].replace("Bearer ", "")
    # Validate token
    if verifyAccessToken(token):
     # Retrieve token scopes
        scopeClaims = token.claims.scp
        # Generate IAM Policy
        iamPolicy = generateIAMPolicy(scopeClaims)
    # Generate default deny all policy statement if there is an error
    policyStatements = []
    policyStatement = generatePolicyStatement("*", "*", "*", "*", "Deny")
    policyStatements.push(policyStatement)
    iamPolicy = generatePolicy('user', policyStatements)

    return iamPolicy

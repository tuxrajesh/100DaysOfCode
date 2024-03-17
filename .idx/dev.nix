{ pkgs, ... }: {

  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    
  ];

  # Sets environment variables in the workspace
  env = {
    SOME_ENV_VAR = "rajesh";
  };
}
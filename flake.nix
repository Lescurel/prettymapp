{
  description = "A basic flake using pyproject.toml project metadata";

  inputs = {
    pyproject-nix = {
      url = "github:nix-community/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
      
    };
  };

  outputs = { nixpkgs, pyproject-nix, ... }:
    let
      inherit (nixpkgs) lib;

      project = pyproject-nix.lib.project.loadPyproject {
        # Read & unmarshal pyproject.toml relative to this project root.
        # projectRoot is also used to set `src` for renderers such as buildPythonPackage.
        projectRoot = ./.;
      };

      # This example is only using x86_64-linux
      pkgs = nixpkgs.legacyPackages.x86_64-linux;

      python = pkgs.python3;

    in
    {
      # Create a development shell containing dependencies from `pyproject.toml`
      devShells.x86_64-linux.default =
        let
          # Returns a function that can be passed to `python.withPackages`
          arg = project.renderers.withPackages { inherit python; };

          # Returns a wrapped environment (virtualenv like) with all our packages
          pythonEnv = python.withPackages arg;

        in
        # Create a devShell like normal.
        pkgs.mkShell { packages = [ pythonEnv ]; };
        
      # Build our package using `buildPythonPackage
      packages.x86_64-linux.default =
        let
          # Returns an attribute set that can be passed to `buildPythonPackage`.
          attrs = project.renderers.buildPythonPackage { inherit python; };
        in
        # Pass attributes to buildPythonPackage.
        # Here is a good spot to add on any missing or custom attributes.
        python.pkgs.buildPythonPackage (attrs // {
          env.CUSTOM_ENVVAR = "hello";
        });
    };
}
